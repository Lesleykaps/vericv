#!/usr/bin/env node
"use strict";

const { spawnSync } = require("node:child_process");
const process = require("node:process");

const REPOSITORY = "https://github.com/Lesleykaps/vericv.git";
const MARKETPLACE = "cipher-technologies-vericv";
const PLUGIN = "vericv";

function usage(exitCode = 0) {
  const output = `
VeriCV installer

Usage:
  npx @ciphertechnologies/vericv <codex|claude> [--yes]

Examples:
  npx @ciphertechnologies/vericv codex
  npx @ciphertechnologies/vericv claude --yes

This installer adds the Cipher Technologies VeriCV marketplace and installs VeriCV.
It never reads or transmits CVs, job descriptions, or candidate data.\n`;
  (exitCode === 0 ? process.stdout : process.stderr).write(output);
  process.exit(exitCode);
}

function run(command, args) {
  const options = { stdio: "inherit", shell: false };
  const result = process.platform === "win32"
    ? spawnSync(process.env.ComSpec || "cmd.exe", ["/d", "/c", [command, ...args].join(" ")], options)
    : spawnSync(command, args, options);
  if (result.error && result.error.code === "ENOENT") {
    throw new Error(`${command} was not found. Install ${command === "codex" ? "Codex CLI/Desktop" : "Claude Code"} first, then try again.`);
  }
  return result.status === 0;
}

function confirm() {
  if (process.argv.includes("--yes")) return Promise.resolve(true);
  if (!process.stdin.isTTY) return Promise.resolve(false);
  process.stdout.write("This will configure a marketplace and install VeriCV. Continue? [y/N] ");
  return new Promise((resolve) => {
    process.stdin.setEncoding("utf8");
    process.stdin.once("data", (value) => resolve(/^y(es)?$/i.test(String(value).trim())));
  });
}

async function main() {
  const target = process.argv.slice(2).find((argument) => !argument.startsWith("-"));
  if (!target || process.argv.includes("--help") || process.argv.includes("-h")) usage();
  if (!["codex", "claude"].includes(target)) {
    process.stderr.write("Choose either 'codex' or 'claude'.\n");
    usage(1);
  }
  if (!(await confirm())) {
    process.stdout.write("Cancelled. No changes were made.\n");
    process.exit(0);
  }

  const addArgs = target === "codex"
    ? ["plugin", "marketplace", "add", REPOSITORY, "--ref", "main"]
    : ["plugin", "marketplace", "add", "Lesleykaps/vericv"];
  const refreshArgs = target === "codex"
    ? ["plugin", "marketplace", "upgrade", MARKETPLACE]
    : ["plugin", "marketplace", "update", MARKETPLACE];
  const installArgs = target === "codex"
    ? ["plugin", "add", `${PLUGIN}@${MARKETPLACE}`]
    : ["plugin", "install", `${PLUGIN}@${MARKETPLACE}`];

  process.stdout.write(`\nAdding the ${MARKETPLACE} marketplace…\n`);
  if (!run(target, addArgs)) process.stdout.write("Marketplace add returned a message. It may already be configured; continuing with refresh.\n");
  process.stdout.write("Refreshing the marketplace…\n");
  if (!run(target, refreshArgs)) throw new Error("VeriCV marketplace could not be refreshed. Check the marketplace command output above and try again.");
  process.stdout.write("Installing VeriCV…\n");
  if (!run(target, installArgs)) throw new Error("VeriCV could not be installed. Check the marketplace command output above and try again.");

  const invoke = target === "codex" ? "$vericv:vericv" : "/vericv:vericv";
  process.stdout.write(`\nInstalled successfully. In a new ${target === "codex" ? "Codex" : "Claude Code"} chat, use ${invoke}.\n`);
}

main().catch((error) => {
  process.stderr.write(`\nInstallation failed: ${error.message}\n`);
  process.exit(1);
});
