#!/bin/bash
set -euo pipefail

# Claude Code Docs Uninstaller v0.2.0

DOCS_DIR="$HOME/claude-code-docs"
CACHE_DIR="$HOME/Library/Caches/claude-code-docs-mirror"
SUPPORT_DIR="$HOME/Library/Application Support/claude-code-docs"
PLIST_LABEL="com.mrkhachaturovclaude-code-docs"
PLIST_FILE="$HOME/Library/LaunchAgents/$PLIST_LABEL.plist"
SKILL_DIR="$HOME/.claude/skills/claude-code-docs"
RULE_FILE="$HOME/.claude/rules/claude-code-docs.md"

echo "Claude Code Docs Uninstaller"
echo "============================"
echo ""
echo "This will remove:"
echo "  • launchd job:    $PLIST_LABEL"
echo "  • plist:          $PLIST_FILE"
echo "  • sync support:   $SUPPORT_DIR"
echo "  • cache clone:    $CACHE_DIR"
echo "  • docs folder:    $DOCS_DIR"
echo "  • skill:          $SKILL_DIR"
echo "  • rule:           $RULE_FILE"
echo "  • legacy /docs command (if present)"
echo ""
read -p "Continue? (y/N): " -n 1 -r
echo
[[ ! $REPLY =~ ^[Yy]$ ]] && { echo "Cancelled."; exit 0; }

launchctl bootout "gui/$UID/$PLIST_LABEL" 2>/dev/null && echo "✓ launchd job unloaded" || echo "  (launchd job not loaded)"
rm -f "$PLIST_FILE" && echo "✓ Removed $PLIST_FILE"
rm -rf "$SUPPORT_DIR" && echo "✓ Removed $SUPPORT_DIR"
rm -rf "$CACHE_DIR" && echo "✓ Removed $CACHE_DIR"
rm -rf "$DOCS_DIR" && echo "✓ Removed $DOCS_DIR"
rm -rf "$SKILL_DIR" && echo "✓ Removed $SKILL_DIR"
rm -f "$RULE_FILE" && echo "✓ Removed $RULE_FILE"
[[ -f "$HOME/.claude/commands/docs.md" ]] && rm -f "$HOME/.claude/commands/docs.md" && echo "✓ Removed legacy /docs command"

echo ""
echo "Uninstall complete."
echo ""
echo "To reinstall:"
echo "  curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/claude-code-docs/main/install.sh | bash"
