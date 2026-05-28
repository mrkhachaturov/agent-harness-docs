#!/bin/bash
set -euo pipefail

# Agent Harness Docs Uninstaller v0.5.0

CLAUDE_DOCS_DIR="$HOME/claude-code-docs"
CODEX_DOCS_DIR="$HOME/codex-docs"
OPENCODE_DOCS_DIR="$HOME/opencode-docs"
PI_DOCS_DIR="$HOME/pi-docs"

CACHE_DIR="$HOME/Library/Caches/agent-harness-docs-mirror"
SUPPORT_DIR="$HOME/Library/Application Support/agent-harness-docs"
PLIST_LABEL="com.mrkhachaturov.agent-harness-docs"
PLIST_FILE="$HOME/Library/LaunchAgents/$PLIST_LABEL.plist"

CLAUDE_SKILL_DIR="$HOME/.claude/skills/claude-code-docs"
CLAUDE_RULE_FILE="$HOME/.claude/rules/claude-code-docs.md"
CODEX_SKILL_DIR="$HOME/.agents/skills/codex-docs"
OPENCODE_SKILL_DIR="$HOME/.agents/skills/opencode-docs"
OPENCODE_SKILL_CLAUDE_LINK="$HOME/.claude/skills/opencode-docs"
PI_SKILL_DIR="$HOME/.agents/skills/pi-docs"
PI_SKILL_CLAUDE_LINK="$HOME/.claude/skills/pi-docs"

# Legacy paths from v0.2.x
LEGACY_CACHE_DIR="$HOME/Library/Caches/claude-code-docs-mirror"
LEGACY_SUPPORT_DIR="$HOME/Library/Application Support/claude-code-docs"
LEGACY_PLIST_LABEL="com.mrkhachaturovclaude-code-docs"
LEGACY_PLIST_FILE="$HOME/Library/LaunchAgents/$LEGACY_PLIST_LABEL.plist"

echo "Agent Harness Docs Uninstaller"
echo "=============================="
echo ""
echo "This will remove:"
echo "  • launchd job:       $PLIST_LABEL (+ legacy $LEGACY_PLIST_LABEL if present)"
echo "  • plists:            $PLIST_FILE, $LEGACY_PLIST_FILE (if any)"
echo "  • sync support:      $SUPPORT_DIR (+ legacy $LEGACY_SUPPORT_DIR)"
echo "  • cache clones:      $CACHE_DIR (+ legacy $LEGACY_CACHE_DIR)"
echo "  • Claude Code docs:  $CLAUDE_DOCS_DIR"
echo "  • Codex docs:        $CODEX_DOCS_DIR"
echo "  • OpenCode docs:     $OPENCODE_DOCS_DIR"
echo "  • Pi docs:           $PI_DOCS_DIR"
echo "  • Claude skill:      $CLAUDE_SKILL_DIR"
echo "  • Claude rule:       $CLAUDE_RULE_FILE"
echo "  • Codex skill:       $CODEX_SKILL_DIR"
echo "  • OpenCode skill:    $OPENCODE_SKILL_DIR"
echo "  • Claude link:       $OPENCODE_SKILL_CLAUDE_LINK (symlink)"
echo "  • Pi skill:          $PI_SKILL_DIR"
echo "  • Claude link:       $PI_SKILL_CLAUDE_LINK (symlink)"
echo "  • legacy /docs command (if present)"
echo ""
echo "What is NOT removed:"
echo "  • Miyo MCP registrations in claude/codex CLIs (you may use Miyo elsewhere)."
echo "    To remove: claude mcp remove miyo  /  codex mcp remove miyo"
echo "  • The Miyo block inside ~/.config/opencode/opencode.json[c]"
echo "    (edit the file manually to drop it — see the \"mcp\" → \"miyo\" entry)"
echo ""
read -p "Continue? (y/N): " -n 1 -r
echo
[[ ! $REPLY =~ ^[Yy]$ ]] && { echo "Cancelled."; exit 0; }

# Current install
launchctl bootout "gui/$UID/$PLIST_LABEL" 2>/dev/null && echo "✓ launchd job unloaded" || echo "  (launchd job not loaded)"
rm -f "$PLIST_FILE" && echo "✓ Removed $PLIST_FILE"
rm -rf "$SUPPORT_DIR" && echo "✓ Removed $SUPPORT_DIR"
rm -rf "$CACHE_DIR" && echo "✓ Removed $CACHE_DIR"
rm -rf "$CLAUDE_DOCS_DIR" && echo "✓ Removed $CLAUDE_DOCS_DIR"
rm -rf "$CODEX_DOCS_DIR" && echo "✓ Removed $CODEX_DOCS_DIR"
rm -rf "$OPENCODE_DOCS_DIR" && echo "✓ Removed $OPENCODE_DOCS_DIR"
rm -rf "$PI_DOCS_DIR" && echo "✓ Removed $PI_DOCS_DIR"
rm -rf "$CLAUDE_SKILL_DIR" && echo "✓ Removed $CLAUDE_SKILL_DIR"
rm -f "$CLAUDE_RULE_FILE" && echo "✓ Removed $CLAUDE_RULE_FILE"
rm -rf "$CODEX_SKILL_DIR" && echo "✓ Removed $CODEX_SKILL_DIR"
# Remove symlink first (rm -rf on a symlink to a dir would delete the target's contents)
[[ -L "$OPENCODE_SKILL_CLAUDE_LINK" ]] && rm -f "$OPENCODE_SKILL_CLAUDE_LINK" && echo "✓ Removed $OPENCODE_SKILL_CLAUDE_LINK"
rm -rf "$OPENCODE_SKILL_DIR" && echo "✓ Removed $OPENCODE_SKILL_DIR"
[[ -L "$PI_SKILL_CLAUDE_LINK" ]] && rm -f "$PI_SKILL_CLAUDE_LINK" && echo "✓ Removed $PI_SKILL_CLAUDE_LINK"
rm -rf "$PI_SKILL_DIR" && echo "✓ Removed $PI_SKILL_DIR"

# Legacy install
launchctl bootout "gui/$UID/$LEGACY_PLIST_LABEL" 2>/dev/null && echo "✓ Legacy launchd job unloaded" || true
rm -f "$LEGACY_PLIST_FILE" && echo "✓ Removed legacy plist"
rm -rf "$LEGACY_SUPPORT_DIR" && echo "✓ Removed legacy support dir"
rm -rf "$LEGACY_CACHE_DIR" && echo "✓ Removed legacy cache dir"

[[ -f "$HOME/.claude/commands/docs.md" ]] && rm -f "$HOME/.claude/commands/docs.md" && echo "✓ Removed legacy /docs command"

echo ""
echo "Uninstall complete."
echo ""
echo "To reinstall:"
echo "  curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/agent-harness-docs/main/install.sh | bash"
