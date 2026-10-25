<!DOCTYPE html>

<html lang="en">
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>ZENVIA INDUS</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0 solid transparent;
  border-right: 0 solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0 solid transparent;
  border-bottom: 0 solid transparent;
}

/*
 * Lumino
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-CommandPalette-search {
  flex: 0 0 auto;
}

.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}

.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}

.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}

.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
  border: 1px solid transparent;
  background-color: transparent;
  position: absolute;
  z-index: 1;
  right: 3%;
  top: 0;
  bottom: 0;
  margin: auto;
  padding: 7px 0;
  display: none;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
  content: 'X';
  display: block;
  width: 15px;
  height: 15px;
  text-align: center;
  color: #000;
  font-weight: normal;
  font-size: 12px;
  cursor: pointer;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-DockPanel {
  z-index: 0;
}

.lm-DockPanel-widget {
  z-index: 0;
}

.lm-DockPanel-tabBar {
  z-index: 1;
}

.lm-DockPanel-handle {
  z-index: 2;
}

.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}

.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}

.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}

.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}

.lm-Menu-item {
  display: table-row;
}

.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}

.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}

.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}

.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}

.lm-MenuBar-item {
  box-sizing: border-box;
}

.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}

.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}

.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}

.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}

.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-SplitPanel-child {
  z-index: 0;
}

.lm-SplitPanel-handle {
  z-index: 1;
}

.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}

.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}

.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}

.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}

.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
  touch-action: none; /* Disable native Drag/Drop */
}

.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
}

.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
  background: inherit;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabPanel-tabBar {
  z-index: 1;
}

.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jp-Collapse-header {
  padding: 1px 12px;
  background-color: var(--jp-layout-color1);
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  text-transform: uppercase;
  user-select: none;
}

.jp-Collapser-icon {
  height: 16px;
}

.jp-Collapse-header-collapsed .jp-Collapser-icon {
  transform: rotate(-90deg);
  margin: auto 0;
}

.jp-Collapser-title {
  line-height: 25px;
}

.jp-Collapse-contents {
  padding: 0 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add-above: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5MikiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik00Ljc1IDQuOTMwNjZINi42MjVWNi44MDU2NkM2LjYyNSA3LjAxMTkxIDYuNzkzNzUgNy4xODA2NiA3IDcuMTgwNjZDNy4yMDYyNSA3LjE4MDY2IDcuMzc1IDcuMDExOTEgNy4zNzUgNi44MDU2NlY0LjkzMDY2SDkuMjVDOS40NTYyNSA0LjkzMDY2IDkuNjI1IDQuNzYxOTEgOS42MjUgNC41NTU2NkM5LjYyNSA0LjM0OTQxIDkuNDU2MjUgNC4xODA2NiA5LjI1IDQuMTgwNjZINy4zNzVWMi4zMDU2NkM3LjM3NSAyLjA5OTQxIDcuMjA2MjUgMS45MzA2NiA3IDEuOTMwNjZDNi43OTM3NSAxLjkzMDY2IDYuNjI1IDIuMDk5NDEgNi42MjUgMi4zMDU2NlY0LjE4MDY2SDQuNzVDNC41NDM3NSA0LjE4MDY2IDQuMzc1IDQuMzQ5NDEgNC4zNzUgNC41NTU2NkM0LjM3NSA0Ljc2MTkxIDQuNTQzNzUgNC45MzA2NiA0Ljc1IDQuOTMwNjZaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC43Ii8+CjwvZz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjUgOS41VjExLjVMMi41IDExLjVWOS41TDExLjUgOS41Wk0xMiA4QzEyLjU1MjMgOCAxMyA4LjQ0NzcyIDEzIDlWMTJDMTMgMTIuNTUyMyAxMi41NTIzIDEzIDEyIDEzTDIgMTNDMS40NDc3MiAxMyAxIDEyLjU1MjMgMSAxMlY5QzEgOC40NDc3MiAxLjQ0NzcxIDggMiA4TDEyIDhaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5MiI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDEwIDEuNTU1NjYpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==);
  --jp-icon-add-below: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5OCkiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik05LjI1IDEwLjA2OTNMNy4zNzUgMTAuMDY5M0w3LjM3NSA4LjE5NDM0QzcuMzc1IDcuOTg4MDkgNy4yMDYyNSA3LjgxOTM0IDcgNy44MTkzNEM2Ljc5Mzc1IDcuODE5MzQgNi42MjUgNy45ODgwOSA2LjYyNSA4LjE5NDM0TDYuNjI1IDEwLjA2OTNMNC43NSAxMC4wNjkzQzQuNTQzNzUgMTAuMDY5MyA0LjM3NSAxMC4yMzgxIDQuMzc1IDEwLjQ0NDNDNC4zNzUgMTAuNjUwNiA0LjU0Mzc1IDEwLjgxOTMgNC43NSAxMC44MTkzTDYuNjI1IDEwLjgxOTNMNi42MjUgMTIuNjk0M0M2LjYyNSAxMi45MDA2IDYuNzkzNzUgMTMuMDY5MyA3IDEzLjA2OTNDNy4yMDYyNSAxMy4wNjkzIDcuMzc1IDEyLjkwMDYgNy4zNzUgMTIuNjk0M0w3LjM3NSAxMC44MTkzTDkuMjUgMTAuODE5M0M5LjQ1NjI1IDEwLjgxOTMgOS42MjUgMTAuNjUwNiA5LjYyNSAxMC40NDQzQzkuNjI1IDEwLjIzODEgOS40NTYyNSAxMC4wNjkzIDkuMjUgMTAuMDY5M1oiIGZpbGw9IiM2MTYxNjEiIHN0cm9rZT0iIzYxNjE2MSIgc3Ryb2tlLXdpZHRoPSIwLjciLz4KPC9nPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDUuNUwyLjUgMy41TDExLjUgMy41TDExLjUgNS41TDIuNSA1LjVaTTIgN0MxLjQ0NzcyIDcgMSA2LjU1MjI4IDEgNkwxIDNDMSAyLjQ0NzcyIDEuNDQ3NzIgMiAyIDJMMTIgMkMxMi41NTIzIDIgMTMgMi40NDc3MiAxMyAzTDEzIDZDMTMgNi41NTIyOSAxMi41NTIzIDcgMTIgN0wyIDdaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5OCI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KDEgMS43NDg0NmUtMDcgMS43NDg0NmUtMDcgLTEgNCAxMy40NDQzKSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=);
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bell: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiB2ZXJzaW9uPSIxLjEiPgogICA8cGF0aCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzMzMzMzIgogICAgICBkPSJtOCAwLjI5Yy0xLjQgMC0yLjcgMC43My0zLjYgMS44LTEuMiAxLjUtMS40IDMuNC0xLjUgNS4yLTAuMTggMi4yLTAuNDQgNC0yLjMgNS4zbDAuMjggMS4zaDVjMC4wMjYgMC42NiAwLjMyIDEuMSAwLjcxIDEuNSAwLjg0IDAuNjEgMiAwLjYxIDIuOCAwIDAuNTItMC40IDAuNi0xIDAuNzEtMS41aDVsMC4yOC0xLjNjLTEuOS0wLjk3LTIuMi0zLjMtMi4zLTUuMy0wLjEzLTEuOC0wLjI2LTMuNy0xLjUtNS4yLTAuODUtMS0yLjItMS44LTMuNi0xLjh6bTAgMS40YzAuODggMCAxLjkgMC41NSAyLjUgMS4zIDAuODggMS4xIDEuMSAyLjcgMS4yIDQuNCAwLjEzIDEuNyAwLjIzIDMuNiAxLjMgNS4yaC0xMGMxLjEtMS42IDEuMi0zLjQgMS4zLTUuMiAwLjEzLTEuNyAwLjMtMy4zIDEuMi00LjQgMC41OS0wLjcyIDEuNi0xLjMgMi41LTEuM3ptLTAuNzQgMTJoMS41Yy0wLjAwMTUgMC4yOCAwLjAxNSAwLjc5LTAuNzQgMC43OS0wLjczIDAuMDAxNi0wLjcyLTAuNTMtMC43NC0wLjc5eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-bug-dot: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiPgogICAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTcuMTkgOEgyMFYxMEgxNy45MUMxNy45NiAxMC4zMyAxOCAxMC42NiAxOCAxMVYxMkgyMFYxNEgxOC41SDE4VjE0LjAyNzVDMTUuNzUgMTQuMjc2MiAxNCAxNi4xODM3IDE0IDE4LjVDMTQgMTkuMjA4IDE0LjE2MzUgMTkuODc3OSAxNC40NTQ5IDIwLjQ3MzlDMTMuNzA2MyAyMC44MTE3IDEyLjg3NTcgMjEgMTIgMjFDOS43OCAyMSA3Ljg1IDE5Ljc5IDYuODEgMThINFYxNkg2LjA5QzYuMDQgMTUuNjcgNiAxNS4zNCA2IDE1VjE0SDRWMTJINlYxMUM2IDEwLjY2IDYuMDQgMTAuMzMgNi4wOSAxMEg0VjhINi44MUM3LjI2IDcuMjIgNy44OCA2LjU1IDguNjIgNi4wNEw3IDQuNDFMOC40MSAzTDEwLjU5IDUuMTdDMTEuMDQgNS4wNiAxMS41MSA1IDEyIDVDMTIuNDkgNSAxMi45NiA1LjA2IDEzLjQyIDUuMTdMMTUuNTkgM0wxNyA0LjQxTDE1LjM3IDYuMDRDMTYuMTIgNi41NSAxNi43NCA3LjIyIDE3LjE5IDhaTTEwIDE2SDE0VjE0SDEwVjE2Wk0xMCAxMkgxNFYxMEgxMFYxMloiIGZpbGw9IiM2MTYxNjEiLz4KICAgICAgICA8cGF0aCBkPSJNMjIgMTguNUMyMiAyMC40MzMgMjAuNDMzIDIyIDE4LjUgMjJDMTYuNTY3IDIyIDE1IDIwLjQzMyAxNSAxOC41QzE1IDE2LjU2NyAxNi41NjcgMTUgMTguNSAxNUMyMC40MzMgMTUgMjIgMTYuNTY3IDIyIDE4LjVaIiBmaWxsPSIjNjE2MTYxIi8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CiAgICA8cGF0aCBkPSJNNi41OSwzLjQxTDIsOEw2LjU5LDEyLjZMOCwxMS4xOEw0LjgyLDhMOCw0LjgyTDYuNTksMy40MU0xMi40MSwzLjQxTDExLDQuODJMMTQuMTgsOEwxMSwxMS4xOEwxMi40MSwxMi42TDE3LDhMMTIuNDEsMy40MU0yMS41OSwxMS41OUwxMy41LDE5LjY4TDkuODMsMTZMOC40MiwxNy40MUwxMy41LDIyLjVMMjMsMTNMMjEuNTksMTEuNTlaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-collapse-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNNiAxM3YyaDh2LTJ6IiAvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1jb25zb2xlLWljb24tYmFja2dyb3VuZC1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtY29uc29sZS1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIj4KICAgIDxwYXRoIGQ9Ik0xMDUgMTI3LjNoNDB2MTIuOGgtNDB6TTUxLjEgNzdMNzQgOTkuOWwtMjMuMyAyMy4zIDEwLjUgMTAuNSAyMy4zLTIzLjNMOTUgOTkuOSA4NC41IDg5LjQgNjEuNiA2Ni41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-delete: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCI+CiAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjI2MjYyIiBkPSJNNiAxOWMwIDEuMS45IDIgMiAyaDhjMS4xIDAgMi0uOSAyLTJWN0g2djEyek0xOSA0aC0zLjVsLTEtMWgtNWwtMSAxSDV2MmgxNFY0eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-duplicate: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIuNzk5OTggMC44NzVIOC44OTU4MkM5LjIwMDYxIDAuODc1IDkuNDQ5OTggMS4xMzkxNCA5LjQ0OTk4IDEuNDYxOThDOS40NDk5OCAxLjc4NDgyIDkuMjAwNjEgMi4wNDg5NiA4Ljg5NTgyIDIuMDQ4OTZIMy4zNTQxNUMzLjA0OTM2IDIuMDQ4OTYgMi43OTk5OCAyLjMxMzEgMi43OTk5OCAyLjYzNTk0VjkuNjc5NjlDMi43OTk5OCAxMC4wMDI1IDIuNTUwNjEgMTAuMjY2NyAyLjI0NTgyIDEwLjI2NjdDMS45NDEwMyAxMC4yNjY3IDEuNjkxNjUgMTAuMDAyNSAxLjY5MTY1IDkuNjc5NjlWMi4wNDg5NkMxLjY5MTY1IDEuNDAzMjggMi4xOTA0IDAuODc1IDIuNzk5OTggMC44NzVaTTUuMzY2NjUgMTEuOVY0LjU1SDExLjA4MzNWMTEuOUg1LjM2NjY1Wk00LjE0MTY1IDQuMTQxNjdDNC4xNDE2NSAzLjY5MDYzIDQuNTA3MjggMy4zMjUgNC45NTgzMiAzLjMyNUgxMS40OTE3QzExLjk0MjcgMy4zMjUgMTIuMzA4MyAzLjY5MDYzIDEyLjMwODMgNC4xNDE2N1YxMi4zMDgzQzEyLjMwODMgMTIuNzU5NCAxMS45NDI3IDEzLjEyNSAxMS40OTE3IDEzLjEyNUg0Ljk1ODMyQzQuNTA3MjggMTMuMTI1IDQuMTQxNjUgMTIuNzU5NCA0LjE0MTY1IDEyLjMwODNWNC4xNDE2N1oiIGZpbGw9IiM2MTYxNjEiLz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNOS40MzU3NCA4LjI2NTA3SDguMzY0MzFWOS4zMzY1QzguMzY0MzEgOS40NTQzNSA4LjI2Nzg4IDkuNTUwNzggOC4xNTAwMiA5LjU1MDc4QzguMDMyMTcgOS41NTA3OCA3LjkzNTc0IDkuNDU0MzUgNy45MzU3NCA5LjMzNjVWOC4yNjUwN0g2Ljg2NDMxQzYuNzQ2NDUgOC4yNjUwNyA2LjY1MDAyIDguMTY4NjQgNi42NTAwMiA4LjA1MDc4QzYuNjUwMDIgNy45MzI5MiA2Ljc0NjQ1IDcuODM2NSA2Ljg2NDMxIDcuODM2NUg3LjkzNTc0VjYuNzY1MDdDNy45MzU3NCA2LjY0NzIxIDguMDMyMTcgNi41NTA3OCA4LjE1MDAyIDYuNTUwNzhDOC4yNjc4OCA2LjU1MDc4IDguMzY0MzEgNi42NDcyMSA4LjM2NDMxIDYuNzY1MDdWNy44MzY1SDkuNDM1NzRDOS41NTM2IDcuODM2NSA5LjY1MDAyIDcuOTMyOTIgOS42NTAwMiA4LjA1MDc4QzkuNjUwMDIgOC4xNjg2NCA5LjU1MzYgOC4yNjUwNyA5LjQzNTc0IDguMjY1MDdaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC41Ii8+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-error: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjE5IiByPSIyIi8+PHBhdGggZD0iTTEwIDNoNHYxMmgtNHoiLz48L2c+CjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiLz4KPC9zdmc+Cg==);
  --jp-icon-expand-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNMTEgMTBIOXYzSDZ2MmgzdjNoMnYtM2gzdi0yaC0zeiIgLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-dot: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWRvdCIgZmlsbD0iI0ZGRiI+CiAgICA8Y2lyY2xlIGN4PSIxOCIgY3k9IjE3IiByPSIzIj48L2NpcmNsZT4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-filter: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-folder-favorite: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6IiBmaWxsPSJub25lIi8+PHBhdGggY2xhc3M9ImpwLWljb24zIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxNjE2MSIgZD0iTTIwIDZoLThsLTItMkg0Yy0xLjEgMC0yIC45LTIgMnYxMmMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjhjMC0xLjEtLjktMi0yLTJ6bS0yLjA2IDExTDE1IDE1LjI4IDEyLjA2IDE3bC43OC0zLjMzLTIuNTktMi4yNCAzLjQxLS4yOUwxNSA4bDEuMzQgMy4xNCAzLjQxLjI5LTIuNTkgMi4yNC43OCAzLjMzeiIvPgo8L3N2Zz4K);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-home: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xMCAyMHYtNmg0djZoNXYtOGgzTDEyIDMgMiAxMmgzdjh6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUwLjk3OCA1MC45NzgiPgoJPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KCQk8cGF0aCBkPSJNNDMuNTIsNy40NThDMzguNzExLDIuNjQ4LDMyLjMwNywwLDI1LjQ4OSwwQzE4LjY3LDAsMTIuMjY2LDIuNjQ4LDcuNDU4LDcuNDU4CgkJCWMtOS45NDMsOS45NDEtOS45NDMsMjYuMTE5LDAsMzYuMDYyYzQuODA5LDQuODA5LDExLjIxMiw3LjQ1NiwxOC4wMzEsNy40NThjMCwwLDAuMDAxLDAsMC4wMDIsMAoJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoKCQkJIE00Mi4xMDYsNDIuMTA1Yy00LjQzMiw0LjQzMS0xMC4zMzIsNi44NzItMTYuNjE1LDYuODcyaC0wLjAwMmMtNi4yODUtMC4wMDEtMTIuMTg3LTIuNDQxLTE2LjYxNy02Ljg3MgoJCQljLTkuMTYyLTkuMTYzLTkuMTYyLTI0LjA3MSwwLTMzLjIzM0MxMy4zMDMsNC40NCwxOS4yMDQsMiwyNS40ODksMmM2LjI4NCwwLDEyLjE4NiwyLjQ0LDE2LjYxNyw2Ljg3MgoJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4KCQk8cGF0aCBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1MwoJCQljMC40NjgtMC41MzYsMC45MjMtMS4wNjIsMS4zNjctMS41NzVjMC42MjYtMC43NTMsMS4xMDQtMS40NzgsMS40MzYtMi4xNzVjMC4zMzEtMC43MDcsMC40OTUtMS41NDEsMC40OTUtMi41CgkJCWMwLTEuMDk2LTAuMjYtMi4wODgtMC43NzktMi45NzljLTAuNTY1LTAuODc5LTEuNTAxLTEuMzM2LTIuODA2LTEuMzY5Yy0xLjgwMiwwLjA1Ny0yLjk4NSwwLjY2Ny0zLjU1LDEuODMyCgkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkKCQkJYzEuMDYyLTEuNjQsMi44NTUtMi40ODEsNS4zNzgtMi41MjdjMi4xNiwwLjAyMywzLjg3NCwwLjYwOCw1LjE0MSwxLjc1OGMxLjI3OCwxLjE2LDEuOTI5LDIuNzY0LDEuOTUsNC44MTEKCQkJYzAsMS4xNDItMC4xMzcsMi4xMTEtMC40MSwyLjkxMWMtMC4zMDksMC44NDUtMC43MzEsMS41OTMtMS4yNjgsMi4yNDNjLTAuNDkyLDAuNjUtMS4wNjgsMS4zMTgtMS43MywyLjAwMgoJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5CgkJCUMyNi41ODksMzIuMjE4LDIzLjU3OCwzMi4yMTgsMjMuNTc4LDMyLjIxOHogTTIzLjU3OCwzOC4yMnYtMy40ODRoMy4wNzZ2My40ODRIMjMuNTc4eiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaW5zcGVjdG9yLWljb24tY29sb3IganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtanNvbi1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0Y5QTgyNSI+CiAgICA8cGF0aCBkPSJNMjAuMiAxMS44Yy0xLjYgMC0xLjcuNS0xLjcgMSAwIC40LjEuOS4xIDEuMy4xLjUuMS45LjEgMS4zIDAgMS43LTEuNCAyLjMtMy41IDIuM2gtLjl2LTEuOWguNWMxLjEgMCAxLjQgMCAxLjQtLjggMC0uMyAwLS42LS4xLTEgMC0uNC0uMS0uOC0uMS0xLjIgMC0xLjMgMC0xLjggMS4zLTItMS4zLS4yLTEuMy0uNy0xLjMtMiAwLS40LjEtLjguMS0xLjIuMS0uNC4xLS43LjEtMSAwLS44LS40LS43LTEuNC0uOGgtLjVWNC4xaC45YzIuMiAwIDMuNS43IDMuNSAyLjMgMCAuNC0uMS45LS4xIDEuMy0uMS41LS4xLjktLjEgMS4zIDAgLjUuMiAxIDEuNyAxdjEuOHpNMS44IDEwLjFjMS42IDAgMS43LS41IDEuNy0xIDAtLjQtLjEtLjktLjEtMS4zLS4xLS41LS4xLS45LS4xLTEuMyAwLTEuNiAxLjQtMi4zIDMuNS0yLjNoLjl2MS45aC0uNWMtMSAwLTEuNCAwLTEuNC44IDAgLjMgMCAuNi4xIDEgMCAuMi4xLjYuMSAxIDAgMS4zIDAgMS44LTEuMyAyQzYgMTEuMiA2IDExLjcgNiAxM2MwIC40LS4xLjgtLjEgMS4yLS4xLjMtLjEuNy0uMSAxIDAgLjguMy44IDEuNC44aC41djEuOWgtLjljLTIuMSAwLTMuNS0uNi0zLjUtMi4zIDAtLjQuMS0uOS4xLTEuMy4xLS41LjEtLjkuMS0xLjMgMC0uNS0uMi0xLTEuNy0xdi0xLjl6Ii8+CiAgICA8Y2lyY2xlIGN4PSIxMSIgY3k9IjEzLjgiIHI9IjIuMSIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSI4LjIiIHI9IjIuMSIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgPGcgY2xhc3M9ImpwLWp1cHl0ZXItaWNvbi1jb2xvciIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgIDxnIGNsYXNzPSJqcC1qdXB5dGVyLWljb24tY29sb3IiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launch: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIgMzIiIHdpZHRoPSIzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yNiwyOEg2YTIuMDAyNywyLjAwMjcsMCwwLDEtMi0yVjZBMi4wMDI3LDIuMDAyNywwLDAsMSw2LDRIMTZWNkg2VjI2SDI2VjE2aDJWMjZBMi4wMDI3LDIuMDAyNywwLDAsMSwyNiwyOFoiLz4KICAgIDxwb2x5Z29uIHBvaW50cz0iMjAgMiAyMCA0IDI2LjU4NiA0IDE4IDEyLjU4NiAxOS40MTQgMTQgMjggNS40MTQgMjggMTIgMzAgMTIgMzAgMiAyMCAyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4K);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-move-down: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMTIuNDcxIDcuNTI4OTlDMTIuNzYzMiA3LjIzNjg0IDEyLjc2MzIgNi43NjMxNiAxMi40NzEgNi40NzEwMVY2LjQ3MTAxQzEyLjE3OSA2LjE3OTA1IDExLjcwNTcgNi4xNzg4NCAxMS40MTM1IDYuNDcwNTRMNy43NSAxMC4xMjc1VjEuNzVDNy43NSAxLjMzNTc5IDcuNDE0MjEgMSA3IDFWMUM2LjU4NTc5IDEgNi4yNSAxLjMzNTc5IDYuMjUgMS43NVYxMC4xMjc1TDIuNTk3MjYgNi40NjgyMkMyLjMwMzM4IDYuMTczODEgMS44MjY0MSA2LjE3MzU5IDEuNTMyMjYgNi40Njc3NFY2LjQ2Nzc0QzEuMjM4MyA2Ljc2MTcgMS4yMzgzIDcuMjM4MyAxLjUzMjI2IDcuNTMyMjZMNi4yOTI4OSAxMi4yOTI5QzYuNjgzNDIgMTIuNjgzNCA3LjMxNjU4IDEyLjY4MzQgNy43MDcxMSAxMi4yOTI5TDEyLjQ3MSA3LjUyODk5WiIgZmlsbD0iIzYxNjE2MSIvPgo8L3N2Zz4K);
  --jp-icon-move-up: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMS41Mjg5OSA2LjQ3MTAxQzEuMjM2ODQgNi43NjMxNiAxLjIzNjg0IDcuMjM2ODQgMS41Mjg5OSA3LjUyODk5VjcuNTI4OTlDMS44MjA5NSA3LjgyMDk1IDIuMjk0MjYgNy44MjExNiAyLjU4NjQ5IDcuNTI5NDZMNi4yNSAzLjg3MjVWMTIuMjVDNi4yNSAxMi42NjQyIDYuNTg1NzkgMTMgNyAxM1YxM0M3LjQxNDIxIDEzIDcuNzUgMTIuNjY0MiA3Ljc1IDEyLjI1VjMuODcyNUwxMS40MDI3IDcuNTMxNzhDMTEuNjk2NiA3LjgyNjE5IDEyLjE3MzYgNy44MjY0MSAxMi40Njc3IDcuNTMyMjZWNy41MzIyNkMxMi43NjE3IDcuMjM4MyAxMi43NjE3IDYuNzYxNyAxMi40Njc3IDYuNDY3NzRMNy43MDcxMSAxLjcwNzExQzcuMzE2NTggMS4zMTY1OCA2LjY4MzQyIDEuMzE2NTggNi4yOTI4OSAxLjcwNzExTDEuNTI4OTkgNi40NzEwMVoiIGZpbGw9IiM2MTYxNjEiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtbm90ZWJvb2staWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iLTEwIC0xMCAxMzEuMTYxMzYxNjk0MzM1OTQgMTMyLjM4ODk5OTkzODk2NDg0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzA2OTk4IiBkPSJNIDU0LjkxODc4NSw5LjE5Mjc0MjFlLTQgQyA1MC4zMzUxMzIsMC4wMjIyMTcyNyA0NS45NTc4NDYsMC40MTMxMzY5NyA0Mi4xMDYyODUsMS4wOTQ2NjkzIDMwLjc2MDA2OSwzLjA5OTE3MzEgMjguNzAwMDM2LDcuMjk0NzcxNCAyOC43MDAwMzUsMTUuMDMyMTY5IHYgMTAuMjE4NzUgaCAyNi44MTI1IHYgMy40MDYyNSBoIC0yNi44MTI1IC0xMC4wNjI1IGMgLTcuNzkyNDU5LDAgLTE0LjYxNTc1ODgsNC42ODM3MTcgLTE2Ljc0OTk5OTgsMTMuNTkzNzUgLTIuNDYxODE5OTgsMTAuMjEyOTY2IC0yLjU3MTAxNTA4LDE2LjU4NjAyMyAwLDI3LjI1IDEuOTA1OTI4Myw3LjkzNzg1MiA2LjQ1NzU0MzIsMTMuNTkzNzQ4IDE0LjI0OTk5OTgsMTMuNTkzNzUgaCA5LjIxODc1IHYgLTEyLjI1IGMgMCwtOC44NDk5MDIgNy42NTcxNDQsLTE2LjY1NjI0OCAxNi43NSwtMTYuNjU2MjUgaCAyNi43ODEyNSBjIDcuNDU0OTUxLDAgMTMuNDA2MjUzLC02LjEzODE2NCAxMy40MDYyNSwtMTMuNjI1IHYgLTI1LjUzMTI1IGMgMCwtNy4yNjYzMzg2IC02LjEyOTk4LC0xMi43MjQ3NzcxIC0xMy40MDYyNSwtMTMuOTM3NDk5NyBDIDY0LjI4MTU0OCwwLjMyNzk0Mzk3IDU5LjUwMjQzOCwtMC4wMjAzNzkwMyA1NC45MTg3ODUsOS4xOTI3NDIxZS00IFogbSAtMTQuNSw4LjIxODc1MDEyNTc5IGMgMi43Njk1NDcsMCA1LjAzMTI1LDIuMjk4NjQ1NiA1LjAzMTI1LDUuMTI0OTk5NiAtMmUtNiwyLjgxNjMzNiAtMi4yNjE3MDMsNS4wOTM3NSAtNS4wMzEyNSw1LjA5Mzc1IC0yLjc3OTQ3NiwtMWUtNiAtNS4wMzEyNSwtMi4yNzc0MTUgLTUuMDMxMjUsLTUuMDkzNzUgLTEwZS03LC0yLjgyNjM1MyAyLjI1MTc3NCwtNS4xMjQ5OTk2IDUuMDMxMjUsLTUuMTI0OTk5NiB6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2ZmZDQzYiIgZD0ibSA4NS42Mzc1MzUsMjguNjU3MTY5IHYgMTEuOTA2MjUgYyAwLDkuMjMwNzU1IC03LjgyNTg5NSwxNi45OTk5OTkgLTE2Ljc1LDE3IGggLTI2Ljc4MTI1IGMgLTcuMzM1ODMzLDAgLTEzLjQwNjI0OSw2LjI3ODQ4MyAtMTMuNDA2MjUsMTMuNjI1IHYgMjUuNTMxMjQ3IGMgMCw3LjI2NjM0NCA2LjMxODU4OCwxMS41NDAzMjQgMTMuNDA2MjUsMTMuNjI1MDA0IDguNDg3MzMxLDIuNDk1NjEgMTYuNjI2MjM3LDIuOTQ2NjMgMjYuNzgxMjUsMCA2Ljc1MDE1NSwtMS45NTQzOSAxMy40MDYyNTMsLTUuODg3NjEgMTMuNDA2MjUsLTEzLjYyNTAwNCBWIDg2LjUwMDkxOSBoIC0yNi43ODEyNSB2IC0zLjQwNjI1IGggMjYuNzgxMjUgMTMuNDA2MjU0IGMgNy43OTI0NjEsMCAxMC42OTYyNTEsLTUuNDM1NDA4IDEzLjQwNjI0MSwtMTMuNTkzNzUgMi43OTkzMywtOC4zOTg4ODYgMi42ODAyMiwtMTYuNDc1Nzc2IDAsLTI3LjI1IC0xLjkyNTc4LC03Ljc1NzQ0MSAtNS42MDM4NywtMTMuNTkzNzUgLTEzLjQwNjI0MSwtMTMuNTkzNzUgeiBtIC0xNS4wNjI1LDY0LjY1NjI1IGMgMi43Nzk0NzgsM2UtNiA1LjAzMTI1LDIuMjc3NDE3IDUuMDMxMjUsNS4wOTM3NDcgLTJlLTYsMi44MjYzNTQgLTIuMjUxNzc1LDUuMTI1MDA0IC01LjAzMTI1LDUuMTI1MDA0IC0yLjc2OTU1LDAgLTUuMDMxMjUsLTIuMjk4NjUgLTUuMDMxMjUsLTUuMTI1MDA0IDJlLTYsLTIuODE2MzMgMi4yNjE2OTcsLTUuMDkzNzQ3IDUuMDMxMjUsLTUuMDkzNzQ3IHoiLz4KPC9zdmc+Cg==);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-share: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTSAxOCAyIEMgMTYuMzU0OTkgMiAxNSAzLjM1NDk5MDQgMTUgNSBDIDE1IDUuMTkwOTUyOSAxNS4wMjE3OTEgNS4zNzcxMjI0IDE1LjA1NjY0MSA1LjU1ODU5MzggTCA3LjkyMTg3NSA5LjcyMDcwMzEgQyA3LjM5ODUzOTkgOS4yNzc4NTM5IDYuNzMyMDc3MSA5IDYgOSBDIDQuMzU0OTkwNCA5IDMgMTAuMzU0OTkgMyAxMiBDIDMgMTMuNjQ1MDEgNC4zNTQ5OTA0IDE1IDYgMTUgQyA2LjczMjA3NzEgMTUgNy4zOTg1Mzk5IDE0LjcyMjE0NiA3LjkyMTg3NSAxNC4yNzkyOTcgTCAxNS4wNTY2NDEgMTguNDM5NDUzIEMgMTUuMDIxNTU1IDE4LjYyMTUxNCAxNSAxOC44MDgzODYgMTUgMTkgQyAxNSAyMC42NDUwMSAxNi4zNTQ5OSAyMiAxOCAyMiBDIDE5LjY0NTAxIDIyIDIxIDIwLjY0NTAxIDIxIDE5IEMgMjEgMTcuMzU0OTkgMTkuNjQ1MDEgMTYgMTggMTYgQyAxNy4yNjc0OCAxNiAxNi42MDE1OTMgMTYuMjc5MzI4IDE2LjA3ODEyNSAxNi43MjI2NTYgTCA4Ljk0MzM1OTQgMTIuNTU4NTk0IEMgOC45NzgyMDk1IDEyLjM3NzEyMiA5IDEyLjE5MDk1MyA5IDEyIEMgOSAxMS44MDkwNDcgOC45NzgyMDk1IDExLjYyMjg3OCA4Ljk0MzM1OTQgMTEuNDQxNDA2IEwgMTYuMDc4MTI1IDcuMjc5Mjk2OSBDIDE2LjYwMTQ2IDcuNzIyMTQ2MSAxNy4yNjc5MjMgOCAxOCA4IEMgMTkuNjQ1MDEgOCAyMSA2LjY0NTAwOTYgMjEgNSBDIDIxIDMuMzU0OTkwNCAxOS42NDUwMSAyIDE4IDIgeiBNIDE4IDQgQyAxOC41NjQxMjkgNCAxOSA0LjQzNTg3MDYgMTkgNSBDIDE5IDUuNTY0MTI5NCAxOC41NjQxMjkgNiAxOCA2IEMgMTcuNDM1ODcxIDYgMTcgNS41NjQxMjk0IDE3IDUgQyAxNyA0LjQzNTg3MDYgMTcuNDM1ODcxIDQgMTggNCB6IE0gNiAxMSBDIDYuNTY0MTI5NCAxMSA3IDExLjQzNTg3MSA3IDEyIEMgNyAxMi41NjQxMjkgNi41NjQxMjk0IDEzIDYgMTMgQyA1LjQzNTg3MDYgMTMgNSAxMi41NjQxMjkgNSAxMiBDIDUgMTEuNDM1ODcxIDUuNDM1ODcwNiAxMSA2IDExIHogTSAxOCAxOCBDIDE4LjU2NDEyOSAxOCAxOSAxOC40MzU4NzEgMTkgMTkgQyAxOSAxOS41NjQxMjkgMTguNTY0MTI5IDIwIDE4IDIwIEMgMTcuNDM1ODcxIDIwIDE3IDE5LjU2NDEyOSAxNyAxOSBDIDE3IDE4LjQzNTg3MSAxNy40MzU4NzEgMTggMTggMTggeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1iYWNrZ3JvdW5kLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyIDIpIiBmaWxsPSIjMzMzMzMzIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUtaW52ZXJzZSIgZD0iTTUuMDU2NjQgOC43NjE3MkM1LjA1NjY0IDguNTk3NjYgNS4wMzEyNSA4LjQ1MzEyIDQuOTgwNDcgOC4zMjgxMkM0LjkzMzU5IDguMTk5MjIgNC44NTU0NyA4LjA4MjAzIDQuNzQ2MDkgNy45NzY1NkM0LjY0MDYyIDcuODcxMDkgNC41IDcuNzc1MzkgNC4zMjQyMiA3LjY4OTQ1QzQuMTUyMzQgNy41OTk2MSAzLjk0MzM2IDcuNTExNzIgMy42OTcyNyA3LjQyNTc4QzMuMzAyNzMgNy4yODUxNiAyLjk0MzM2IDcuMTM2NzIgMi42MTkxNCA2Ljk4MDQ3QzIuMjk0OTIgNi44MjQyMiAyLjAxNzU4IDYuNjQyNTggMS43ODcxMSA2LjQzNTU1QzEuNTYwNTUgNi4yMjg1MiAxLjM4NDc3IDUuOTg4MjggMS4yNTk3NyA1LjcxNDg0QzEuMTM0NzcgNS40Mzc1IDEuMDcyMjcgNS4xMDkzOCAxLjA3MjI3IDQuNzMwNDdDMS4wNzIyNyA0LjM5ODQ0IDEuMTI4OTEgNC4wOTU3IDEuMjQyMTkgMy44MjIyN0MxLjM1NTQ3IDMuNTQ0OTIgMS41MTU2MiAzLjMwNDY5IDEuNzIyNjYgMy4xMDE1NkMxLjkyOTY5IDIuODk4NDQgMi4xNzk2OSAyLjczNDM3IDIuNDcyNjYgMi42MDkzOEMyLjc2NTYyIDIuNDg0MzggMy4wOTE4IDIuNDA0MyAzLjQ1MTE3IDIuMzY5MTRWMS4xMDkzOEg0LjM4ODY3VjIuMzgwODZDNC43NDAyMyAyLjQyNzczIDUuMDU2NjQgMi41MjM0NCA1LjMzNzg5IDIuNjY3OTdDNS42MTkxNCAyLjgxMjUgNS44NTc0MiAzLjAwMTk1IDYuMDUyNzMgMy4yMzYzM0M2LjI1MTk1IDMuNDY2OCA2LjQwNDMgMy43NDAyMyA2LjUwOTc3IDQuMDU2NjRDNi42MTkxNCA0LjM2OTE0IDYuNjczODMgNC43MjA3IDYuNjczODMgNS4xMTEzM0g1LjA0NDkyQzUuMDQ0OTIgNC42Mzg2NyA0LjkzNzUgNC4yODEyNSA0LjcyMjY2IDQuMDM5MDZDNC41MDc4MSAzLjc5Mjk3IDQuMjE2OCAzLjY2OTkyIDMuODQ5NjEgMy42Njk5MkMzLjY1MDM5IDMuNjY5OTIgMy40NzY1NiAzLjY5NzI3IDMuMzI4MTIgMy43NTE5NUMzLjE4MzU5IDMuODAyNzMgMy4wNjQ0NSAzLjg3Njk1IDIuOTcwNyAzLjk3NDYxQzIuODc2OTUgNC4wNjgzNiAyLjgwNjY0IDQuMTc5NjkgMi43NTk3NyA0LjMwODU5QzIuNzE2OCA0LjQzNzUgMi42OTUzMSA0LjU3ODEyIDIuNjk1MzEgNC43MzA0N0MyLjY5NTMxIDQuODgyODEgMi43MTY4IDUuMDE5NTMgMi43NTk3NyA1LjE0MDYyQzIuODA2NjQgNS4yNTc4MSAyLjg4MjgxIDUuMzY3MTkgMi45ODgyOCA1LjQ2ODc1QzMuMDk3NjYgNS41NzAzMSAzLjI0MDIzIDUuNjY3OTcgMy40MTYwMiA1Ljc2MTcyQzMuNTkxOCA1Ljg1MTU2IDMuODEwNTUgNS45NDMzNiA0LjA3MjI3IDYuMDM3MTFDNC40NjY4IDYuMTg1NTUgNC44MjQyMiA2LjMzOTg0IDUuMTQ0NTMgNi41QzUuNDY0ODQgNi42NTYyNSA1LjczODI4IDYuODM5ODQgNS45NjQ4NCA3LjA1MDc4QzYuMTk1MzEgNy4yNTc4MSA2LjM3MTA5IDcuNSA2LjQ5MjE5IDcuNzc3MzRDNi42MTcxOSA4LjA1MDc4IDYuNjc5NjkgOC4zNzUgNi42Nzk2OSA4Ljc1QzYuNjc5NjkgOS4wOTM3NSA2LjYyMzA1IDkuNDA0MyA2LjUwOTc3IDkuNjgxNjRDNi4zOTY0OCA5Ljk1NTA4IDYuMjM0MzggMTAuMTkxNCA2LjAyMzQ0IDEwLjM5MDZDNS44MTI1IDEwLjU4OTggNS41NTg1OSAxMC43NSA1LjI2MTcyIDEwLjg3MTFDNC45NjQ4NCAxMC45ODgzIDQuNjMyODEgMTEuMDY0NSA0LjI2NTYyIDExLjA5OTZWMTIuMjQ4SDMuMzMzOThWMTEuMDk5NkMzLjAwMTk1IDExLjA2ODQgMi42Nzk2OSAxMC45OTYxIDIuMzY3MTkgMTAuODgyOEMyLjA1NDY5IDEwLjc2NTYgMS43NzczNCAxMC41OTc3IDEuNTM1MTYgMTAuMzc4OUMxLjI5Njg4IDEwLjE2MDIgMS4xMDU0NyA5Ljg4NDc3IDAuOTYwOTM4IDkuNTUyNzNDMC44MTY0MDYgOS4yMTY4IDAuNzQ0MTQxIDguODE0NDUgMC43NDQxNDEgOC4zNDU3SDIuMzc4OTFDMi4zNzg5MSA4LjYyNjk1IDIuNDE5OTIgOC44NjMyOCAyLjUwMTk1IDkuMDU0NjlDMi41ODM5OCA5LjI0MjE5IDIuNjg5NDUgOS4zOTI1OCAyLjgxODM2IDkuNTA1ODZDMi45NTExNyA5LjYxNTIzIDMuMTAxNTYgOS42OTMzNiAzLjI2OTUzIDkuNzQwMjNDMy40Mzc1IDkuNzg3MTEgMy42MDkzOCA5LjgxMDU1IDMuNzg1MTYgOS44MTA1NUM0LjIwMzEyIDkuODEwNTUgNC41MTk1MyA5LjcxMjg5IDQuNzM0MzggOS41MTc1OEM0Ljk0OTIyIDkuMzIyMjcgNS4wNTY2NCA5LjA3MDMxIDUuMDU2NjQgOC43NjE3MlpNMTMuNDE4IDEyLjI3MTVIOC4wNzQyMlYxMUgxMy40MThWMTIuMjcxNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuOTUyNjQgNikiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtdGV4dC1lZGl0b3ItaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xNSAxNUgzdjJoMTJ2LTJ6bTAtOEgzdjJoMTJWN3pNMyAxM2gxOHYtMkgzdjJ6bTAgOGgxOHYtMkgzdjJ6TTMgM3YyaDE4VjNIM3oiLz4KPC9zdmc+Cg==);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-user: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE2IDdhNCA0IDAgMTEtOCAwIDQgNCAwIDAxOCAwek0xMiAxNGE3IDcgMCAwMC03IDdoMTRhNyA3IDAgMDAtNy03eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-users: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDM2IDI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGcgY2xhc3M9ImpwLWljb24zIiB0cmFuc2Zvcm09Im1hdHJpeCgxLjczMjcgMCAwIDEuNzMyNyAtMy42MjgyIC4wOTk1NzcpIiBmaWxsPSIjNjE2MTYxIj4KICA8cGF0aCB0cmFuc2Zvcm09Im1hdHJpeCgxLjUsMCwwLDEuNSwwLC02KSIgZD0ibTEyLjE4NiA3LjUwOThjLTEuMDUzNSAwLTEuOTc1NyAwLjU2NjUtMi40Nzg1IDEuNDEwMiAwLjc1MDYxIDAuMzEyNzcgMS4zOTc0IDAuODI2NDggMS44NzMgMS40NzI3aDMuNDg2M2MwLTEuNTkyLTEuMjg4OS0yLjg4MjgtMi44ODA5LTIuODgyOHoiLz4KICA8cGF0aCBkPSJtMjAuNDY1IDIuMzg5NWEyLjE4ODUgMi4xODg1IDAgMCAxLTIuMTg4NCAyLjE4ODUgMi4xODg1IDIuMTg4NSAwIDAgMS0yLjE4ODUtMi4xODg1IDIuMTg4NSAyLjE4ODUgMCAwIDEgMi4xODg1LTIuMTg4NSAyLjE4ODUgMi4xODg1IDAgMCAxIDIuMTg4NCAyLjE4ODV6Ii8+CiAgPHBhdGggdHJhbnNmb3JtPSJtYXRyaXgoMS41LDAsMCwxLjUsMCwtNikiIGQ9Im0zLjU4OTggOC40MjE5Yy0xLjExMjYgMC0yLjAxMzcgMC45MDExMS0yLjAxMzcgMi4wMTM3aDIuODE0NWMwLjI2Nzk3LTAuMzczMDkgMC41OTA3LTAuNzA0MzUgMC45NTg5OC0wLjk3ODUyLTAuMzQ0MzMtMC42MTY4OC0xLjAwMzEtMS4wMzUyLTEuNzU5OC0xLjAzNTJ6Ii8+CiAgPHBhdGggZD0ibTYuOTE1NCA0LjYyM2ExLjUyOTQgMS41Mjk0IDAgMCAxLTEuNTI5NCAxLjUyOTQgMS41Mjk0IDEuNTI5NCAwIDAgMS0xLjUyOTQtMS41Mjk0IDEuNTI5NCAxLjUyOTQgMCAwIDEgMS41Mjk0LTEuNTI5NCAxLjUyOTQgMS41Mjk0IDAgMCAxIDEuNTI5NCAxLjUyOTR6Ii8+CiAgPHBhdGggZD0ibTYuMTM1IDEzLjUzNWMwLTMuMjM5MiAyLjYyNTktNS44NjUgNS44NjUtNS44NjUgMy4yMzkyIDAgNS44NjUgMi42MjU5IDUuODY1IDUuODY1eiIvPgogIDxjaXJjbGUgY3g9IjEyIiBjeT0iMy43Njg1IiByPSIyLjk2ODUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-word: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KIDxnIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzQxNDE0MSI+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiA8L2c+CiA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguNDMgLjA0MDEpIiBmaWxsPSIjZmZmIj4KICA8cGF0aCBkPSJtNC4xNCA4Ljc2cTAuMDY4Mi0xLjg5IDIuNDItMS44OSAxLjE2IDAgMS42OCAwLjQyIDAuNTY3IDAuNDEgMC41NjcgMS4xNnYzLjQ3cTAgMC40NjIgMC41MTQgMC40NjIgMC4xMDMgMCAwLjItMC4wMjMxdjAuNzE0cS0wLjM5OSAwLjEwMy0wLjY1MSAwLjEwMy0wLjQ1MiAwLTAuNjkzLTAuMjItMC4yMzEtMC4yLTAuMjg0LTAuNjYyLTAuOTU2IDAuODcyLTIgMC44NzItMC45MDMgMC0xLjQ3LTAuNDcyLTAuNTI1LTAuNDcyLTAuNTI1LTEuMjYgMC0wLjI2MiAwLjA0NTItMC40NzIgMC4wNTY3LTAuMjIgMC4xMTYtMC4zNzggMC4wNjgyLTAuMTY4IDAuMjMxLTAuMzA0IDAuMTU4LTAuMTQ3IDAuMjYyLTAuMjQyIDAuMTE2LTAuMDkxNCAwLjM2OC0wLjE2OCAwLjI2Mi0wLjA5MTQgMC4zOTktMC4xMjYgMC4xMzYtMC4wNDUyIDAuNDcyLTAuMTAzIDAuMzM2LTAuMDU3OCAwLjUwNC0wLjA3OTggMC4xNTgtMC4wMjMxIDAuNTY3LTAuMDc5OCAwLjU1Ni0wLjA2ODIgMC43NzctMC4yMjEgMC4yMi0wLjE1MiAwLjIyLTAuNDQxdi0wLjI1MnEwLTAuNDMtMC4zNTctMC42NjItMC4zMzYtMC4yMzEtMC45NzYtMC4yMzEtMC42NjIgMC0wLjk5OCAwLjI2Mi0wLjMzNiAwLjI1Mi0wLjM5OSAwLjc5OHptMS44OSAzLjY4cTAuNzg4IDAgMS4yNi0wLjQxIDAuNTA0LTAuNDIgMC41MDQtMC45MDN2LTEuMDVxLTAuMjg0IDAuMTM2LTAuODYxIDAuMjMxLTAuNTY3IDAuMDkxNC0wLjk4NyAwLjE1OC0wLjQyIDAuMDY4Mi0wLjc2NiAwLjMyNi0wLjMzNiAwLjI1Mi0wLjMzNiAwLjcwNHQwLjMwNCAwLjcwNCAwLjg2MSAwLjI1MnoiIHN0cm9rZS13aWR0aD0iMS4wNSIvPgogIDxwYXRoIGQ9Im0xMCA0LjU2aDAuOTQ1djMuMTVxMC42NTEtMC45NzYgMS44OS0wLjk3NiAxLjE2IDAgMS44OSAwLjg0IDAuNjgyIDAuODQgMC42ODIgMi4zMSAwIDEuNDctMC43MDQgMi40Mi0wLjcwNCAwLjg4Mi0xLjg5IDAuODgyLTEuMjYgMC0xLjg5LTEuMDJ2MC43NjZoLTAuODV6bTIuNjIgMy4wNHEtMC43NDYgMC0xLjE2IDAuNjQtMC40NTIgMC42My0wLjQ1MiAxLjY4IDAgMS4wNSAwLjQ1MiAxLjY4dDEuMTYgMC42M3EwLjc3NyAwIDEuMjYtMC42MyAwLjQ5NC0wLjY0IDAuNDk0LTEuNjggMC0xLjA1LTAuNDcyLTEuNjgtMC40NjItMC42NC0xLjI2LTAuNjR6IiBzdHJva2Utd2lkdGg9IjEuMDUiLz4KICA8cGF0aCBkPSJtMi43MyAxNS44IDEzLjYgMC4wMDgxYzAuMDA2OSAwIDAtMi42IDAtMi42IDAtMC4wMDc4LTEuMTUgMC0xLjE1IDAtMC4wMDY5IDAtMC4wMDgzIDEuNS0wLjAwODMgMS41LTJlLTMgLTAuMDAxNC0xMS4zLTAuMDAxNC0xMS4zLTAuMDAxNGwtMC4wMDU5Mi0xLjVjMC0wLjAwNzgtMS4xNyAwLjAwMTMtMS4xNyAwLjAwMTN6IiBzdHJva2Utd2lkdGg9Ii45NzUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddAboveIcon {
  background-image: var(--jp-icon-add-above);
}

.jp-AddBelowIcon {
  background-image: var(--jp-icon-add-below);
}

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}

.jp-BellIcon {
  background-image: var(--jp-icon-bell);
}

.jp-BugDotIcon {
  background-image: var(--jp-icon-bug-dot);
}

.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}

.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}

.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}

.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}

.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}

.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}

.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}

.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}

.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}

.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}

.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}

.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}

.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}

.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}

.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}

.jp-CodeCheckIcon {
  background-image: var(--jp-icon-code-check);
}

.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}

.jp-CollapseAllIcon {
  background-image: var(--jp-icon-collapse-all);
}

.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}

.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}

.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}

.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}

.jp-DeleteIcon {
  background-image: var(--jp-icon-delete);
}

.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}

.jp-DuplicateIcon {
  background-image: var(--jp-icon-duplicate);
}

.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}

.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}

.jp-ErrorIcon {
  background-image: var(--jp-icon-error);
}

.jp-ExpandAllIcon {
  background-image: var(--jp-icon-expand-all);
}

.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}

.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}

.jp-FileIcon {
  background-image: var(--jp-icon-file);
}

.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}

.jp-FilterDotIcon {
  background-image: var(--jp-icon-filter-dot);
}

.jp-FilterIcon {
  background-image: var(--jp-icon-filter);
}

.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}

.jp-FolderFavoriteIcon {
  background-image: var(--jp-icon-folder-favorite);
}

.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}

.jp-HomeIcon {
  background-image: var(--jp-icon-home);
}

.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}

.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}

.jp-InfoIcon {
  background-image: var(--jp-icon-info);
}

.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}

.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}

.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}

.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}

.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}

.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}

.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}

.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}

.jp-LaunchIcon {
  background-image: var(--jp-icon-launch);
}

.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}

.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}

.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}

.jp-ListIcon {
  background-image: var(--jp-icon-list);
}

.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}

.jp-MoveDownIcon {
  background-image: var(--jp-icon-move-down);
}

.jp-MoveUpIcon {
  background-image: var(--jp-icon-move-up);
}

.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}

.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}

.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}

.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}

.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}

.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}

.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}

.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}

.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}

.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}

.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}

.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}

.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}

.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}

.jp-RunIcon {
  background-image: var(--jp-icon-run);
}

.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}

.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}

.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}

.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}

.jp-ShareIcon {
  background-image: var(--jp-icon-share);
}

.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}

.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}

.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}

.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}

.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}

.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}

.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}

.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}

.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}

.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}

.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}

.jp-UserIcon {
  background-image: var(--jp-icon-user);
}

.jp-UsersIcon {
  background-image: var(--jp-icon-users);
}

.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}

.jp-WordIcon {
  background-image: var(--jp-icon-word);
}

.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-TabBar .lm-TabBar-addButton {
  align-items: center;
  display: flex;
  padding: 4px;
  padding-bottom: 5px;
  margin-right: 1px;
  background-color: var(--jp-layout-color2);
}

.lm-TabBar .lm-TabBar-addButton:hover {
  background-color: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar-tab {
  width: var(--jp-private-horizontal-tab-width);
}

.lm-DockPanel-tabBar .lm-TabBar-content {
  flex: unset;
}

.lm-DockPanel-tabBar[data-orientation='horizontal'] {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}

/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}

.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}

.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}

.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}

.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}

.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}

.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}

.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}

.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}

/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}

.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}

.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}

.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}

.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}

.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}

.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}

/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

.jp-icon-dot[fill] {
  fill: var(--jp-warn-color0);
}

.jp-jupyter-icon-color[fill] {
  fill: var(--jp-jupyter-icon-color, var(--jp-warn-color0));
}

.jp-notebook-icon-color[fill] {
  fill: var(--jp-notebook-icon-color, var(--jp-warn-color0));
}

.jp-json-icon-color[fill] {
  fill: var(--jp-json-icon-color, var(--jp-warn-color1));
}

.jp-console-icon-color[fill] {
  fill: var(--jp-console-icon-color, white);
}

.jp-console-icon-background-color[fill] {
  fill: var(--jp-console-icon-background-color, var(--jp-brand-color1));
}

.jp-terminal-icon-color[fill] {
  fill: var(--jp-terminal-icon-color, var(--jp-layout-color2));
}

.jp-terminal-icon-background-color[fill] {
  fill: var(
    --jp-terminal-icon-background-color,
    var(--jp-inverse-layout-color2)
  );
}

.jp-text-editor-icon-color[fill] {
  fill: var(--jp-text-editor-icon-color, var(--jp-inverse-layout-color3));
}

.jp-inspector-icon-color[fill] {
  fill: var(--jp-inspector-icon-color, var(--jp-inverse-layout-color3));
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* stylelint-disable selector-max-class, selector-max-compound-selectors */

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}

.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* stylelint-enable selector-max-class, selector-max-compound-selectors */

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) .jp-icon-hoverShow-content {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FormGroup-content fieldset {
  border: none;
  padding: 0;
  min-width: 0;
  width: 100%;
}

/* stylelint-disable selector-max-type */

.jp-FormGroup-content fieldset .jp-inputFieldWrapper input,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper select,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper textarea {
  font-size: var(--jp-content-font-size2);
  border-color: var(--jp-input-border-color);
  border-style: solid;
  border-radius: var(--jp-border-radius);
  border-width: 1px;
  padding: 6px 8px;
  background: none;
  color: var(--jp-ui-font-color0);
  height: inherit;
}

.jp-FormGroup-content fieldset input[type='checkbox'] {
  position: relative;
  top: 2px;
  margin-left: 0;
}

.jp-FormGroup-content button.jp-mod-styled {
  cursor: pointer;
}

.jp-FormGroup-content .checkbox label {
  cursor: pointer;
  font-size: var(--jp-content-font-size1);
}

.jp-FormGroup-content .jp-root > fieldset > legend {
  display: none;
}

.jp-FormGroup-content .jp-root > fieldset > p {
  display: none;
}

/** copy of `input.jp-mod-styled:focus` style */
.jp-FormGroup-content fieldset input:focus,
.jp-FormGroup-content fieldset select:focus {
  -moz-outline-radius: unset;
  outline: var(--jp-border-width) solid var(--md-blue-500);
  outline-offset: -1px;
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FormGroup-content fieldset input:hover:not(:focus),
.jp-FormGroup-content fieldset select:hover:not(:focus) {
  background-color: var(--jp-border-color2);
}

/* stylelint-enable selector-max-type */

.jp-FormGroup-content .checkbox .field-description {
  /* Disable default description field for checkbox:
   because other widgets do not have description fields,
   we add descriptions to each widget on the field level.
  */
  display: none;
}

.jp-FormGroup-content #root__description {
  display: none;
}

.jp-FormGroup-content .jp-modifiedIndicator {
  width: 5px;
  background-color: var(--jp-brand-color2);
  margin-top: 0;
  margin-left: calc(var(--jp-private-settingeditor-modifier-indent) * -1);
  flex-shrink: 0;
}

.jp-FormGroup-content .jp-modifiedIndicator.jp-errorIndicator {
  background-color: var(--jp-error-color0);
  margin-right: 0.5em;
}

/* RJSF ARRAY style */

.jp-arrayFieldWrapper legend {
  font-size: var(--jp-content-font-size2);
  color: var(--jp-ui-font-color0);
  flex-basis: 100%;
  padding: 4px 0;
  font-weight: var(--jp-content-heading-font-weight);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-arrayFieldWrapper .field-description {
  padding: 4px 0;
  white-space: pre-wrap;
}

.jp-arrayFieldWrapper .array-item {
  width: 100%;
  border: 1px solid var(--jp-border-color2);
  border-radius: 4px;
  margin: 4px;
}

.jp-ArrayOperations {
  display: flex;
  margin-left: 8px;
}

.jp-ArrayOperationsButton {
  margin: 2px;
}

.jp-ArrayOperationsButton .jp-icon3[fill] {
  fill: var(--jp-ui-font-color0);
}

button.jp-ArrayOperationsButton.jp-mod-styled:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

/* RJSF form validation error */

.jp-FormGroup-content .validationErrors {
  color: var(--jp-error-color0);
}

/* Hide panel level error as duplicated the field level error */
.jp-FormGroup-content .panel.errors {
  display: none;
}

/* RJSF normal content (settings-editor) */

.jp-FormGroup-contentNormal {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-FormGroup-contentItem {
  margin-left: 7px;
  color: var(--jp-ui-font-color0);
}

.jp-FormGroup-contentNormal .jp-FormGroup-description {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-default {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-fieldLabel {
  font-size: var(--jp-content-font-size1);
  font-weight: normal;
  min-width: 120px;
}

.jp-FormGroup-contentNormal fieldset:not(:first-child) {
  margin-left: 7px;
}

.jp-FormGroup-contentNormal .field-array-of-string .array-item {
  /* Display `jp-ArrayOperations` buttons side-by-side with content except
    for small screens where flex-wrap will place them one below the other.
  */
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-objectFieldWrapper .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

/* RJSF compact content (metadata-form) */

.jp-FormGroup-content.jp-FormGroup-contentCompact {
  width: 100%;
}

.jp-FormGroup-contentCompact .form-group {
  display: flex;
  padding: 0.5em 0.2em 0.5em 0;
}

.jp-FormGroup-contentCompact
  .jp-FormGroup-compactTitle
  .jp-FormGroup-description {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color2);
}

.jp-FormGroup-contentCompact .jp-FormGroup-fieldLabel {
  padding-bottom: 0.3em;
}

.jp-FormGroup-contentCompact .jp-inputFieldWrapper .form-control {
  width: 100%;
  box-sizing: border-box;
}

.jp-FormGroup-contentCompact .jp-arrayFieldWrapper .jp-FormGroup-compactTitle {
  padding-bottom: 7px;
}

.jp-FormGroup-contentCompact
  .jp-objectFieldWrapper
  .jp-objectFieldWrapper
  .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

.jp-FormGroup-contentCompact ul.error-detail {
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  padding-inline-start: 1em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-SidePanel {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
  overflow-y: auto;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size1);
}

.jp-SidePanel-header {
  flex: 0 0 auto;
  display: flex;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0;
  padding: 2px;
  text-transform: uppercase;
}

.jp-SidePanel-toolbar {
  flex: 0 0 auto;
}

.jp-SidePanel-content {
  flex: 1 1 auto;
}

.jp-SidePanel-toolbar,
.jp-AccordionPanel-toolbar {
  height: var(--jp-private-toolbar-height);
}

.jp-SidePanel-toolbar.jp-Toolbar-micro {
  display: none;
}

.lm-AccordionPanel .jp-AccordionPanel-title {
  box-sizing: border-box;
  line-height: 25px;
  margin: 0;
  display: flex;
  align-items: center;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  font-size: var(--jp-ui-font-size0);
}

.jp-AccordionPanel-title {
  cursor: pointer;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  text-transform: uppercase;
}

.lm-AccordionPanel[data-orientation='horizontal'] > .jp-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleLabel {
  user-select: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleCollapser {
  transform: rotate(-90deg);
  margin: auto 0;
  height: 16px;
}

.jp-AccordionPanel-title.lm-mod-expanded .lm-AccordionPanel-titleCollapser {
  transform: rotate(0deg);
}

.lm-AccordionPanel .jp-AccordionPanel-toolbar {
  background: none;
  box-shadow: none;
  border: none;
  margin-left: auto;
}

.lm-AccordionPanel .lm-SplitPanel-handle:hover {
  background: var(--jp-layout-color3);
}

.jp-text-truncated {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent::before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent::after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper:not(.multiple) {
  height: 28px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

select.jp-mod-styled:not([multiple]) {
  height: 32px;
}

select.jp-mod-styled[multiple] {
  max-height: 200px;
  overflow-y: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
  font-family: var(--jp-ui-font-family);
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-switch-color, var(--jp-border-color1));
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-switch-true-position-color, var(--jp-warn-color0));
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 8;
  overflow-x: hidden;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0;
  margin: 0;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0 6px;
  margin: 0;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent > span {
  padding: 0;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-WindowedPanel-outer {
  position: relative;
  overflow-y: auto;
}

.jp-WindowedPanel-inner {
  position: relative;
}

.jp-WindowedPanel-window {
  position: absolute;
  left: 0;
  right: 0;
  overflow: visible;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

body {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

/* Disable native link decoration styles everywhere outside of dialog boxes */
a {
  text-decoration: unset;
  color: unset;
}

a:hover {
  text-decoration: unset;
  color: unset;
}

/* Accessibility for links inside dialog box text */
.jp-Dialog-content a {
  text-decoration: revert;
  color: var(--jp-content-link-color);
}

.jp-Dialog-content a:hover {
  text-decoration: revert;
}

/* Styles for ui-components */
.jp-Button {
  color: var(--jp-ui-font-color2);
  border-radius: var(--jp-border-radius);
  padding: 0 12px;
  font-size: var(--jp-ui-font-size1);

  /* Copy from blueprint 3 */
  display: inline-flex;
  flex-direction: row;
  border: none;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  text-align: left;
  vertical-align: middle;
  min-height: 30px;
  min-width: 30px;
}

.jp-Button:disabled {
  cursor: not-allowed;
}

.jp-Button:empty {
  padding: 0 !important;
}

.jp-Button.jp-mod-small {
  min-height: 24px;
  min-width: 24px;
  font-size: 12px;
  padding: 0 7px;
}

/* Use our own theme for hover styles */
.jp-Button.jp-mod-minimal:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Button.jp-mod-minimal {
  background: none;
}

.jp-InputGroup {
  display: block;
  position: relative;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border: none;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
  padding-bottom: 0;
  padding-top: 0;
  padding-left: 10px;
  padding-right: 28px;
  position: relative;
  width: 100%;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  font-size: 14px;
  font-weight: 400;
  height: 30px;
  line-height: 30px;
  outline: none;
  vertical-align: middle;
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input:disabled {
  cursor: not-allowed;
  resize: block;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input:disabled ~ span {
  cursor: not-allowed;
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color2);
}

.jp-InputGroupAction {
  position: absolute;
  bottom: 1px;
  right: 0;
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
  cursor: not-allowed;
  resize: block;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled ~ span {
  cursor: not-allowed;
}

/* Use our own theme for hover and option styles */
/* stylelint-disable-next-line selector-max-type */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}

select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-StatusBar-Widget {
  display: flex;
  align-items: center;
  background: var(--jp-layout-color2);
  min-height: var(--jp-statusbar-height);
  justify-content: space-between;
  padding: 0 10px;
}

.jp-StatusBar-Left {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-StatusBar-Middle {
  display: flex;
  align-items: center;
}

.jp-StatusBar-Right {
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
}

.jp-StatusBar-Item {
  max-height: var(--jp-statusbar-height);
  margin: 0 2px;
  height: var(--jp-statusbar-height);
  white-space: nowrap;
  text-overflow: ellipsis;
  color: var(--jp-ui-font-color1);
  padding: 0 6px;
}

.jp-mod-highlighted:hover {
  background-color: var(--jp-layout-color3);
}

.jp-mod-clicked {
  background-color: var(--jp-brand-color1);
}

.jp-mod-clicked:hover {
  background-color: var(--jp-brand-color0);
}

.jp-mod-clicked .jp-StatusBar-TextItem {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-StatusBar-HoverItem {
  box-shadow: '0px 4px 4px rgba(0, 0, 0, 0.25)';
}

.jp-StatusBar-TextItem {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  line-height: 24px;
  color: var(--jp-ui-font-color1);
}

.jp-StatusBar-GroupItem {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-Statusbar-ProgressCircle svg {
  display: block;
  margin: 0 auto;
  width: 16px;
  height: 24px;
  align-self: normal;
}

.jp-Statusbar-ProgressCircle path {
  fill: var(--jp-inverse-layout-color3);
}

.jp-Statusbar-ProgressBar-progress-bar {
  height: 10px;
  width: 100px;
  border: solid 0.25px var(--jp-brand-color2);
  border-radius: 3px;
  overflow: hidden;
  align-self: center;
}

.jp-Statusbar-ProgressBar-progress-bar > div {
  background-color: var(--jp-brand-color2);
  background-image: linear-gradient(
    -45deg,
    rgba(255, 255, 255, 0.2) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.2) 75%,
    transparent 75%,
    transparent
  );
  background-size: 40px 40px;
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 14px;
  color: #fff;
  text-align: center;
  animation: jp-Statusbar-ExecutionTime-progress-bar 2s linear infinite;
}

.jp-Statusbar-ProgressBar-progress-bar p {
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
  font-size: var(--jp-ui-font-size1);
  line-height: 10px;
  width: 100px;
}

@keyframes jp-Statusbar-ExecutionTime-progress-bar {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: 40px 40px;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty::after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px 24px 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-content.jp-Dialog-content-small {
  max-width: 500px;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus {
  outline: 1px solid var(--jp-accept-color-normal, var(--jp-brand-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus {
  outline: 1px solid var(--jp-warn-color-normal, var(--jp-error-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline: 1px solid var(--jp-reject-color-normal, var(--md-grey-600));
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color1);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-checkbox {
  padding-right: 5px;
}

.jp-Dialog-checkbox > input:focus-visible {
  outline: 1px solid var(--jp-input-active-border-color);
  outline-offset: 1px;
}

.jp-Dialog-spacer {
  flex: 1 1 auto;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error {
  padding: 6px;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error > pre {
  width: auto;
  padding: 10px;
  background: var(--jp-error-color3);
  border: var(--jp-border-width) solid var(--jp-error-color1);
  border-radius: var(--jp-border-radius);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  white-space: pre-wrap;
  word-wrap: break-word;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;
  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;
  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #a0f;
  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;
  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;
  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;
  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;
  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;
  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;
  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;
  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;
  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;
  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ff0;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;
  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;
  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;
  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;
  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;
  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;
  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0;
  padding: 0;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}

.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}

.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}

.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}

.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}

.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}

.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}

.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}

.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}

.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}

.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}

.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}

.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}

.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}

.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}

.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}

.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);

  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

/* stylelint-disable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0;
}

/* stylelint-enable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  table-layout: fixed;
  margin-left: auto;
  margin-bottom: 1em;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}

[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}

.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}

.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}

.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}

.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}

.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}

.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}

.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}

.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: var(--jp-ui-font-size0);
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-cursor-backdrop {
  position: fixed;
  width: 200px;
  height: 200px;
  margin-top: -100px;
  margin-left: -100px;
  will-change: transform;
  z-index: 100;
}

.lm-mod-drag-image {
  will-change: transform;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-lineFormSearch {
  padding: 4px 12px;
  background-color: var(--jp-layout-color2);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
  font-size: var(--jp-ui-font-size1);
}

.jp-lineFormCaption {
  font-size: var(--jp-ui-font-size0);
  line-height: var(--jp-ui-font-size1);
  margin-top: 4px;
  color: var(--jp-ui-font-color0);
}

.jp-baseLineForm {
  border: none;
  border-radius: 0;
  position: absolute;
  background-size: 16px;
  background-repeat: no-repeat;
  background-position: center;
  outline: none;
}

.jp-lineFormButtonContainer {
  top: 4px;
  right: 8px;
  height: 24px;
  padding: 0 12px;
  width: 12px;
}

.jp-lineFormButtonIcon {
  top: 0;
  right: 0;
  background-color: var(--jp-brand-color1);
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  padding: 4px 6px;
}

.jp-lineFormButton {
  top: 0;
  right: 0;
  background-color: transparent;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
}

.jp-lineFormWrapper {
  overflow: hidden;
  padding: 0 8px;
  border: 1px solid var(--jp-border-color0);
  background-color: var(--jp-input-active-background);
  height: 22px;
}

.jp-lineFormWrapperFocusWithin {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-lineFormInput {
  background: transparent;
  width: 200px;
  height: 100%;
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  line-height: 28px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
.jp-DocumentSearch-input {
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size1);
  background-color: var(--jp-layout-color0);
  font-family: var(--jp-ui-font-family);
  padding: 2px 1px;
  resize: none;
}

.jp-DocumentSearch-overlay {
  position: absolute;
  background-color: var(--jp-toolbar-background);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  top: 0;
  right: 0;
  z-index: 7;
  min-width: 405px;
  padding: 2px;
  font-size: var(--jp-ui-font-size1);

  --jp-private-document-search-button-height: 20px;
}

.jp-DocumentSearch-overlay button {
  background-color: var(--jp-toolbar-background);
  outline: 0;
}

.jp-DocumentSearch-overlay button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-overlay button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-overlay-row {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
}

.jp-DocumentSearch-button-content {
  display: inline-block;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-button-content svg {
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-input-wrapper {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  margin: 2px;
}

.jp-DocumentSearch-input-wrapper:focus-within {
  border-color: var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper {
  all: initial;
  overflow: hidden;
  display: inline-block;
  border: none;
  box-sizing: border-box;
}

.jp-DocumentSearch-toggle-wrapper {
  width: 14px;
  height: 14px;
}

.jp-DocumentSearch-button-wrapper {
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
}

.jp-DocumentSearch-toggle-wrapper:focus,
.jp-DocumentSearch-button-wrapper:focus {
  outline: var(--jp-border-width) solid
    var(--jp-cell-editor-active-border-color);
  outline-offset: -1px;
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper,
.jp-DocumentSearch-button-content:focus {
  outline: none;
}

.jp-DocumentSearch-toggle-placeholder {
  width: 5px;
}

.jp-DocumentSearch-input-button::before {
  display: block;
  padding-top: 100%;
}

.jp-DocumentSearch-input-button-off {
  opacity: var(--jp-search-toggle-off-opacity);
}

.jp-DocumentSearch-input-button-off:hover {
  opacity: var(--jp-search-toggle-hover-opacity);
}

.jp-DocumentSearch-input-button-on {
  opacity: var(--jp-search-toggle-on-opacity);
}

.jp-DocumentSearch-index-counter {
  padding-left: 10px;
  padding-right: 10px;
  user-select: none;
  min-width: 35px;
  display: inline-block;
}

.jp-DocumentSearch-up-down-wrapper {
  display: inline-block;
  padding-right: 2px;
  margin-left: auto;
  white-space: nowrap;
}

.jp-DocumentSearch-spacer {
  margin-left: auto;
}

.jp-DocumentSearch-up-down-wrapper button {
  outline: 0;
  border: none;
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
  vertical-align: middle;
  margin: 1px 5px 2px;
}

.jp-DocumentSearch-up-down-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-up-down-button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-filter-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-filter-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled:hover {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-search-options {
  padding: 0 8px;
  margin-left: 3px;
  width: 100%;
  display: grid;
  justify-content: start;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-items: stretch;
}

.jp-DocumentSearch-search-filter-disabled {
  color: var(--jp-ui-font-color2);
}

.jp-DocumentSearch-search-filter {
  display: flex;
  align-items: center;
  user-select: none;
}

.jp-DocumentSearch-regex-error {
  color: var(--jp-error-color0);
}

.jp-DocumentSearch-replace-button-wrapper {
  overflow: hidden;
  display: inline-block;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color0);
  margin: auto 2px;
  padding: 1px 4px;
  height: calc(var(--jp-private-document-search-button-height) + 2px);
}

.jp-DocumentSearch-replace-button-wrapper:focus {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-replace-button {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  box-sizing: border-box;
  color: var(--jp-ui-font-color1);

  /* height - 2 * (padding of wrapper) */
  line-height: calc(var(--jp-private-document-search-button-height) - 2px);
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-replace-button:focus {
  outline: none;
}

.jp-DocumentSearch-replace-wrapper-class {
  margin-left: 14px;
  display: flex;
}

.jp-DocumentSearch-replace-toggle {
  border: none;
  background-color: var(--jp-toolbar-background);
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-replace-toggle:hover {
  background-color: var(--jp-layout-color2);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.cm-editor {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;

  /* Changed to auto to autogrow */
}

.cm-editor pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .cm-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

.jp-CodeMirrorEditor {
  cursor: text;
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.cm-editor.jp-mod-readOnly .cm-cursor {
  display: none;
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.cm-searching,
.cm-searching span {
  /* `.cm-searching span`: we need to override syntax highlighting */
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.cm-searching::selection,
.cm-searching span::selection {
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.jp-current-match > .cm-searching,
.jp-current-match > .cm-searching span,
.cm-searching > .jp-current-match,
.cm-searching > .jp-current-match span {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.jp-current-match > .cm-searching::selection,
.cm-searching > .jp-current-match::selection,
.jp-current-match > .cm-searching span::selection {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.cm-trailingspace {
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII=);
  background-position: center left;
  background-repeat: repeat-x;
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .cm-ySelectionCaret {
  position: relative;
  border-left: 1px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret > .cm-ySelectionInfo {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -1px;
  font-size: 0.95em;
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 101;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .cm-ySelectionInfo {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret:hover > .cm-ySelectionInfo {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser .jp-SidePanel-content {
  display: flex;
  flex-direction: column;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  flex-wrap: wrap;
  row-gap: 12px;
  border-bottom: none;
  height: auto;
  margin: 8px 12px 0;
  box-shadow: none;
  padding: 0;
  justify-content: flex-start;
}

.jp-FileBrowser-Panel {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0 2px;
  padding: 0 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0;
  padding-right: 2px;
  align-items: center;
  height: unset;
}

.jp-FileBrowser-toolbar > .jp-Toolbar-item .jp-ToolbarButtonComponent {
  width: 40px;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileSize-hidden {
  display: none;
}

.jp-FileBrowser .lm-AccordionPanel > h3:first-child {
  display: none;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-headerItem.jp-id-filesize {
  flex: 0 0 75px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-checkboxWrapper {
  /* Increases hit area of checkbox. */
  padding: 4px;
}

.jp-DirListing-header
  .jp-DirListing-checkboxWrapper
  + .jp-DirListing-headerItem {
  padding-left: 4px;
}

.jp-DirListing-content .jp-DirListing-checkboxWrapper {
  position: relative;
  left: -4px;
  margin: -4px 0 -4px -8px;
}

.jp-DirListing-checkboxWrapper.jp-mod-visible {
  visibility: visible;
}

/* For devices that support hovering, hide checkboxes until hovered, selected...
*/
@media (hover: hover) {
  .jp-DirListing-checkboxWrapper {
    visibility: hidden;
  }

  .jp-DirListing-item:hover .jp-DirListing-checkboxWrapper,
  .jp-DirListing-item.jp-mod-selected .jp-DirListing-checkboxWrapper {
    visibility: visible;
  }
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemText:focus {
  outline-width: 2px;
  outline-color: var(--jp-inverse-layout-color1);
  outline-style: solid;
  outline-offset: 1px;
}

.jp-DirListing-item.jp-mod-selected .jp-DirListing-itemText:focus {
  outline-color: var(--jp-layout-color1);
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-itemFileSize {
  flex: 0 0 90px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon::before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon::before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-OutputPrompt {
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-prompt {
  display: table-cell;
  vertical-align: top;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea .jp-RenderedText {
  padding-left: 1ch;
}

/**
 * Prompt overlay.
 */

.jp-OutputArea-promptOverlay {
  position: absolute;
  top: 0;
  width: var(--jp-cell-prompt-width);
  height: 100%;
  opacity: 0.5;
}

.jp-OutputArea-promptOverlay:hover {
  background: var(--jp-layout-color2);
  box-shadow: inset 0 0 1px var(--jp-inverse-layout-color0);
  cursor: zoom-out;
}

.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay:hover {
  cursor: zoom-in;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0;
  padding: 0;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

.jp-TrimmedOutputs pre {
  background: var(--jp-layout-color3);
  font-size: calc(var(--jp-code-font-size) * 1.4);
  text-align: center;
  text-transform: uppercase;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/* Hide empty lines in the output area, for instance due to cleared widgets */
.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0;
  width: 100%;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;

  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;

  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0 0.25em;
  margin: 0 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input::placeholder {
  opacity: 0;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

.jp-Stdin-input:focus::placeholder {
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

@media print {
  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-OutputPrompt {
    display: table-row;
    text-align: left;
  }

  .jp-OutputArea-child .jp-OutputArea-output {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }
}

/* Trimmed outputs warning */
.jp-TrimmedOutputs > a {
  margin: 10px;
  text-decoration: none;
  cursor: pointer;
}

.jp-TrimmedOutputs > a:hover {
  text-decoration: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Table of Contents
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toc-active-width: 4px;
}

.jp-TableOfContents {
  display: flex;
  flex-direction: column;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  height: 100%;
}

.jp-TableOfContents-placeholder {
  text-align: center;
}

.jp-TableOfContents-placeholderContent {
  color: var(--jp-content-font-color2);
  padding: 8px;
}

.jp-TableOfContents-placeholderContent > h3 {
  margin-bottom: var(--jp-content-heading-margin-bottom);
}

.jp-TableOfContents .jp-SidePanel-content {
  overflow-y: auto;
}

.jp-TableOfContents-tree {
  margin: 4px;
}

.jp-TableOfContents ol {
  list-style-type: none;
}

/* stylelint-disable-next-line selector-max-type */
.jp-TableOfContents li > ol {
  /* Align left border with triangle icon center */
  padding-left: 11px;
}

.jp-TableOfContents-content {
  /* left margin for the active heading indicator */
  margin: 0 0 0 var(--jp-private-toc-active-width);
  padding: 0;
  background-color: var(--jp-layout-color1);
}

.jp-tocItem {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-tocItem-heading {
  display: flex;
  cursor: pointer;
}

.jp-tocItem-heading:hover {
  background-color: var(--jp-layout-color2);
}

.jp-tocItem-content {
  display: block;
  padding: 4px 0;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow-x: hidden;
}

.jp-tocItem-collapser {
  height: 20px;
  margin: 2px 2px 0;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}

.jp-tocItem-collapser:hover {
  background-color: var(--jp-layout-color3);
}

/* Active heading indicator */

.jp-tocItem-heading::before {
  content: ' ';
  background: transparent;
  width: var(--jp-private-toc-active-width);
  height: 24px;
  position: absolute;
  left: 0;
  border-radius: var(--jp-border-radius);
}

.jp-tocItem-heading.jp-tocItem-active::before {
  background-color: var(--jp-brand-color1);
}

.jp-tocItem-heading:hover.jp-tocItem-active::before {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;

  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Hiding collapsers in print mode.

Note: input and output wrappers have "display: block" propery in print mode.
*/

@media print {
  .jp-Collapser {
    display: none;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0;
  width: 100%;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-InputArea-editor {
  display: table-cell;
  overflow: hidden;
  vertical-align: top;

  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  display: table-cell;
  vertical-align: top;
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-InputArea-editor {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }

  .jp-InputPrompt {
    display: table-row;
    text-align: left;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: table;
  table-layout: fixed;
  width: 100%;
}

.jp-Placeholder-prompt {
  display: table-cell;
  box-sizing: border-box;
}

.jp-Placeholder-content {
  display: table-cell;
  padding: 4px 6px;
  border: 1px solid transparent;
  border-radius: 0;
  background: none;
  box-sizing: border-box;
  cursor: pointer;
}

.jp-Placeholder-contentContainer {
  display: flex;
}

.jp-Placeholder-content:hover,
.jp-InputPlaceholder > .jp-Placeholder-content:hover {
  border-color: var(--jp-layout-color3);
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

.jp-PlaceholderText {
  white-space: nowrap;
  overflow-x: hidden;
  color: var(--jp-inverse-layout-color3);
  font-family: var(--jp-code-font-family);
}

.jp-InputPlaceholder > .jp-Placeholder-content {
  border-color: var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0;
  margin: 0;

  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 24em;
  margin-left: var(--jp-private-cell-scrolling-output-offset);
  resize: vertical;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea[style*='height'] {
  max-height: unset;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea::after {
  content: ' ';
  box-shadow: inset 0 0 6px 2px rgb(0 0 0 / 30%);
  width: 100%;
  height: 100%;
  position: sticky;
  bottom: 0;
  top: 0;
  margin-top: -50%;
  float: left;
  display: block;
  pointer-events: none;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-child {
  padding-top: 6px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay {
  left: calc(-1 * var(--jp-private-cell-scrolling-output-offset));
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  display: table-cell;
  width: 100%;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

/* collapseHeadingButton (show always if hiddenCellsButton is _not_ shown) */
.jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  font-size: var(--jp-code-font-size);
  position: absolute;
  background-color: transparent;
  background-size: 25px;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: top;
  background-image: var(--jp-icon-caret-down);
  right: 0;
  top: 0;
  bottom: 0;
}

.jp-collapseHeadingButton.jp-mod-collapsed {
  background-image: var(--jp-icon-caret-right);
}

/*
 set the container font size to match that of content
 so that the nested collapse buttons have the right size
*/
.jp-MarkdownCell .jp-InputPrompt {
  font-size: var(--jp-content-font-size1);
}

/*
  Align collapseHeadingButton with cell top header
  The font sizes are identical to the ones in packages/rendermime/style/base.css
*/
.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='1'] {
  font-size: var(--jp-content-font-size5);
  background-position-y: calc(0.3 * var(--jp-content-font-size5));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='2'] {
  font-size: var(--jp-content-font-size4);
  background-position-y: calc(0.3 * var(--jp-content-font-size4));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='3'] {
  font-size: var(--jp-content-font-size3);
  background-position-y: calc(0.3 * var(--jp-content-font-size3));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='4'] {
  font-size: var(--jp-content-font-size2);
  background-position-y: calc(0.3 * var(--jp-content-font-size2));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='5'] {
  font-size: var(--jp-content-font-size1);
  background-position-y: top;
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='6'] {
  font-size: var(--jp-content-font-size0);
  background-position-y: top;
}

/* collapseHeadingButton (show only on (hover,active) if hiddenCellsButton is shown) */
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-collapseHeadingButton {
  display: none;
}

.jp-Notebook.jp-mod-showHiddenCellsButton
  :is(.jp-MarkdownCell:hover, .jp-mod-active)
  .jp-collapseHeadingButton {
  display: flex;
}

/* showHiddenCellsButton (only show if jp-mod-showHiddenCellsButton is set, which
is a consequence of the showHiddenCellsButton option in Notebook Settings)*/
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
  display: flex;
}

.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-showHiddenCellsButton {
  display: none;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Using block instead of flex to allow the use of the break-inside CSS property for
cell outputs.
*/

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-notebook-toolbar-padding: 2px 5px 2px 2px;
}

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: var(--jp-notebook-toolbar-padding);

  /* disable paint containment from lumino 2.0 default strict CSS containment */
  contain: style size !important;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

.jp-Toolbar-responsive-popup {
  position: absolute;
  height: fit-content;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: var(--jp-notebook-toolbar-padding);
  z-index: 1;
  right: 0;
  top: 0;
}

.jp-Toolbar > .jp-Toolbar-responsive-opener {
  margin-left: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-Notebook-ExecutionIndicator {
  position: relative;
  display: inline-block;
  height: 100%;
  z-index: 9997;
}

.jp-Notebook-ExecutionIndicator-tooltip {
  visibility: hidden;
  height: auto;
  width: max-content;
  width: -moz-max-content;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color1);
  text-align: justify;
  border-radius: 6px;
  padding: 0 5px;
  position: fixed;
  display: table;
}

.jp-Notebook-ExecutionIndicator-tooltip.up {
  transform: translateX(-50%) translateY(-100%) translateY(-32px);
}

.jp-Notebook-ExecutionIndicator-tooltip.down {
  transform: translateX(calc(-100% + 16px)) translateY(5px);
}

.jp-Notebook-ExecutionIndicator-tooltip.hidden {
  display: none;
}

.jp-Notebook-ExecutionIndicator:hover .jp-Notebook-ExecutionIndicator-tooltip {
  visibility: visible;
}

.jp-Notebook-ExecutionIndicator span {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  color: var(--jp-ui-font-color1);
  line-height: 24px;
  display: block;
}

.jp-Notebook-ExecutionIndicator-progress-bar {
  display: flex;
  justify-content: center;
  height: 100%;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * Execution indicator
 */
.jp-tocItem-content::after {
  content: '';

  /* Must be identical to form a circle */
  width: 12px;
  height: 12px;
  background: none;
  border: none;
  position: absolute;
  right: 0;
}

.jp-tocItem-content[data-running='0']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background: none;
}

.jp-tocItem-content[data-running='1']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background-color: var(--jp-inverse-layout-color3);
}

.jp-tocItem-content[data-running='0'],
.jp-tocItem-content[data-running='1'] {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Notebook-footer {
  height: 27px;
  margin-left: calc(
    var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
      var(--jp-cell-padding)
  );
  width: calc(
    100% -
      (
        var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
          var(--jp-cell-padding) + var(--jp-cell-padding)
      )
  );
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  color: var(--jp-ui-font-color3);
  margin-top: 6px;
  background: none;
  cursor: pointer;
}

.jp-Notebook-footer:focus {
  border-color: var(--jp-cell-editor-active-border-color);
}

/* For devices that support hovering, hide footer until hover */
@media (hover: hover) {
  .jp-Notebook-footer {
    opacity: 0;
  }

  .jp-Notebook-footer:focus,
  .jp-Notebook-footer:hover {
    opacity: 1;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-side-by-side-output-size: 1fr;
  --jp-side-by-side-resized-cell: var(--jp-side-by-side-output-size);
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

/* stylelint-disable selector-max-class */

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}

.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt::before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-ActiveCellTool {
  padding: 12px 0;
  display: flex;
}

.jp-ActiveCellTool-Content {
  flex: 1 1 auto;
}

.jp-ActiveCellTool .jp-ActiveCellTool-CellContent {
  background: var(--jp-cell-editor-background);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  min-height: 29px;
}

.jp-ActiveCellTool .jp-InputPrompt {
  min-width: calc(var(--jp-cell-prompt-width) * 0.75);
}

.jp-ActiveCellTool-CellContent > pre {
  padding: 5px 4px;
  margin: 0;
  white-space: normal;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label,
.jp-NumberSetter label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0;
}

.jp-NumberSetter input {
  width: 100%;
  margin-top: 4px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Side-by-side Mode (.jp-mod-sideBySide)
|----------------------------------------------------------------------------*/
.jp-mod-sideBySide.jp-Notebook .jp-Notebook-cell {
  margin-top: 3em;
  margin-bottom: 3em;
  margin-left: 5%;
  margin-right: 5%;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell {
  display: grid;
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-output-size)
    );
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-template-areas:
    'header header header'
    'input handle output'
    'footer footer footer';
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell.jp-mod-resizedCell {
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-resized-cell)
    );
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellHeader {
  grid-area: header;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-inputWrapper {
  grid-area: input;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-outputWrapper {
  /* overwrite the default margin (no vertical separation needed in side by side move */
  margin-top: 0;
  grid-area: output;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellFooter {
  grid-area: footer;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle {
  grid-area: handle;
  user-select: none;
  display: block;
  height: 100%;
  cursor: ew-resize;
  padding: 0 var(--jp-cell-padding);
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle::after {
  content: '';
  display: block;
  background: var(--jp-border-color2);
  height: 100%;
  width: 5px;
}

.jp-mod-sideBySide.jp-Notebook
  .jp-CodeCell.jp-mod-resizedCell
  .jp-CellResizeHandle::after {
  background: var(--jp-border-color0);
}

.jp-CellResizeHandle {
  display: none;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0 2px 1px -1px var(--jp-shadow-umbra-color),
    0 1px 1px 0 var(--jp-shadow-penumbra-color),
    0 1px 3px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0 3px 1px -2px var(--jp-shadow-umbra-color),
    0 2px 2px 0 var(--jp-shadow-penumbra-color),
    0 1px 5px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0 2px 4px -1px var(--jp-shadow-umbra-color),
    0 4px 5px 0 var(--jp-shadow-penumbra-color),
    0 1px 10px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0 3px 5px -1px var(--jp-shadow-umbra-color),
    0 6px 10px 0 var(--jp-shadow-penumbra-color),
    0 1px 18px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0 5px 5px -3px var(--jp-shadow-umbra-color),
    0 8px 10px 1px var(--jp-shadow-penumbra-color),
    0 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0 7px 8px -4px var(--jp-shadow-umbra-color),
    0 12px 17px 2px var(--jp-shadow-penumbra-color),
    0 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0 8px 10px -5px var(--jp-shadow-umbra-color),
    0 16px 24px 2px var(--jp-shadow-penumbra-color),
    0 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0 10px 13px -6px var(--jp-shadow-umbra-color),
    0 20px 31px 3px var(--jp-shadow-penumbra-color),
    0 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0 11px 15px -7px var(--jp-shadow-umbra-color),
    0 24px 38px 3px var(--jp-shadow-penumbra-color),
    0 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-inverse-border-color: var(--md-grey-600);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;
  --jp-ui-font-family: system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI',
    helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;
  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);
  --jp-content-link-color: var(--md-blue-900);
  --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
    'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: menlo, consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);
  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);
  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);
  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);
  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;
  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);
  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);

  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;

  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-inverse-border-color);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: rgb(0, 54, 109);
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #a2f;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #a2f;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /*
    RTC user specific colors.
    These colors are used for the cursor, username in the editor,
    and the icon of the user.
  */

  --jp-collaborator-color1: #ffad8e;
  --jp-collaborator-color2: #dac83d;
  --jp-collaborator-color3: #72dd76;
  --jp-collaborator-color4: #00e4d0;
  --jp-collaborator-color5: #45d4ff;
  --jp-collaborator-color6: #e2b1ff;
  --jp-collaborator-color7: #ff9de6;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);

  /* Button colors */
  --jp-accept-color-normal: var(--md-blue-700);
  --jp-accept-color-hover: var(--md-blue-800);
  --jp-accept-color-active: var(--md-blue-900);
  --jp-warn-color-normal: var(--md-red-700);
  --jp-warn-color-hover: var(--md-red-800);
  --jp-warn-color-active: var(--md-red-900);
  --jp-reject-color-normal: var(--md-grey-600);
  --jp-reject-color-hover: var(--md-grey-700);
  --jp-reject-color-active: var(--md-grey-800);

  /* File or activity icons and switch semantic variables */
  --jp-jupyter-icon-color: #f37626;
  --jp-notebook-icon-color: #f37626;
  --jp-json-icon-color: var(--md-orange-700);
  --jp-console-icon-background-color: var(--md-blue-700);
  --jp-console-icon-color: white;
  --jp-terminal-icon-background-color: var(--md-grey-800);
  --jp-terminal-icon-color: var(--md-grey-200);
  --jp-text-editor-icon-color: var(--md-grey-700);
  --jp-inspector-icon-color: var(--md-grey-700);
  --jp-switch-color: var(--md-grey-400);
  --jp-switch-true-position-color: var(--md-orange-900);
}
</style>
<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.cm-editor.cm-s-jupyter .highlight pre {
/* weird, but --jp-code-padding defined to be 5px but 4px horizontal padding is hardcoded for pre.cm-line */
  padding: var(--jp-code-padding) 4px;
  margin: 0;

  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  color: inherit;

}

.jp-OutputArea-output pre {
  line-height: inherit;
  font-family: inherit;
}

.jp-RenderedText pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@page {
    margin: 0.5in; /* Margin for each printed piece of paper */
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}
</style>
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                messageStyle: 'none',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
<!-- End of mathjax configuration --><script type="module">
  document.addEventListener("DOMContentLoaded", async () => {
    const diagrams = document.querySelectorAll(".jp-Mermaid > pre.mermaid");
    // do not load mermaidjs if not needed
    if (!diagrams.length) {
      return;
    }
    const mermaid = (await import("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.7.0/mermaid.esm.min.mjs")).default;
    const parser = new DOMParser();

    mermaid.initialize({
      maxTextSize: 100000,
      maxEdges: 100000,
      startOnLoad: false,
      fontFamily: window
        .getComputedStyle(document.body)
        .getPropertyValue("--jp-ui-font-family"),
      theme: document.querySelector("body[data-jp-theme-light='true']")
        ? "default"
        : "dark",
    });

    let _nextMermaidId = 0;

    function makeMermaidImage(svg) {
      const img = document.createElement("img");
      const doc = parser.parseFromString(svg, "image/svg+xml");
      const svgEl = doc.querySelector("svg");
      const { maxWidth } = svgEl?.style || {};
      const firstTitle = doc.querySelector("title");
      const firstDesc = doc.querySelector("desc");

      img.setAttribute("src", `data:image/svg+xml,${encodeURIComponent(svg)}`);
      if (maxWidth) {
        img.width = parseInt(maxWidth);
      }
      if (firstTitle) {
        img.setAttribute("alt", firstTitle.textContent);
      }
      if (firstDesc) {
        const caption = document.createElement("figcaption");
        caption.className = "sr-only";
        caption.textContent = firstDesc.textContent;
        return [img, caption];
      }
      return [img];
    }

    async function makeMermaidError(text) {
      let errorMessage = "";
      try {
        await mermaid.parse(text);
      } catch (err) {
        errorMessage = `${err}`;
      }

      const result = document.createElement("details");
      result.className = 'jp-RenderedMermaid-Details';
      const summary = document.createElement("summary");
      summary.className = 'jp-RenderedMermaid-Summary';
      const pre = document.createElement("pre");
      const code = document.createElement("code");
      code.innerText = text;
      pre.appendChild(code);
      summary.appendChild(pre);
      result.appendChild(summary);

      const warning = document.createElement("pre");
      warning.innerText = errorMessage;
      result.appendChild(warning);
      return [result];
    }

    async function renderOneMarmaid(src) {
      const id = `jp-mermaid-${_nextMermaidId++}`;
      const parent = src.parentNode;
      let raw = src.textContent.trim();
      const el = document.createElement("div");
      el.style.visibility = "hidden";
      document.body.appendChild(el);
      let results = null;
      let output = null;
      try {
        let { svg } = await mermaid.render(id, raw, el);
        svg = cleanMermaidSvg(svg);
        results = makeMermaidImage(svg);
        output = document.createElement("figure");
        results.map(output.appendChild, output);
      } catch (err) {
        parent.classList.add("jp-mod-warning");
        results = await makeMermaidError(raw);
        output = results[0];
      } finally {
        el.remove();
      }
      parent.classList.add("jp-RenderedMermaid");
      parent.appendChild(output);
    }


    /**
     * Post-process to ensure mermaid diagrams contain only valid SVG and XHTML.
     */
    function cleanMermaidSvg(svg) {
      return svg.replace(RE_VOID_ELEMENT, replaceVoidElement);
    }


    /**
     * A regular expression for all void elements, which may include attributes and
     * a slash.
     *
     * @see https://developer.mozilla.org/en-US/docs/Glossary/Void_element
     *
     * Of these, only `<br>` is generated by Mermaid in place of `\n`,
     * but _any_ "malformed" tag will break the SVG rendering entirely.
     */
    const RE_VOID_ELEMENT =
      /<\s*(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\s*([^>]*?)\s*>/gi;

    /**
     * Ensure a void element is closed with a slash, preserving any attributes.
     */
    function replaceVoidElement(match, tag, rest) {
      rest = rest.trim();
      if (!rest.endsWith('/')) {
        rest = `${rest} /`;
      }
      return `<${tag} ${rest}>`;
    }

    void Promise.all([...diagrams].map(renderOneMarmaid));
  });
</script>
<style>
  .jp-Mermaid:not(.jp-RenderedMermaid) {
    display: none;
  }

  .jp-RenderedMermaid {
    overflow: auto;
    display: flex;
  }

  .jp-RenderedMermaid.jp-mod-warning {
    width: auto;
    padding: 0.5em;
    margin-top: 0.5em;
    border: var(--jp-border-width) solid var(--jp-warn-color2);
    border-radius: var(--jp-border-radius);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .jp-RenderedMermaid figure {
    margin: 0;
    overflow: auto;
    max-width: 100%;
  }

  .jp-RenderedMermaid img {
    max-width: 100%;
  }

  .jp-RenderedMermaid-Details > pre {
    margin-top: 1em;
  }

  .jp-RenderedMermaid-Summary {
    color: var(--jp-warn-color2);
  }

  .jp-RenderedMermaid:not(.jp-mod-warning) pre {
    display: none;
  }

  .jp-RenderedMermaid-Summary > pre {
    display: inline-block;
    white-space: normal;
  }
</style>
<!-- End of mermaid configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<main><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=c8e7fe8d-e48f-4b16-ab50-c29ddfc4d597">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">pip</span> install opencv-python mediapipe
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Defaulting to user installation because normal site-packages is not writeable
Collecting opencv-python
  Downloading opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl.metadata (20 kB)
Collecting mediapipe
  Downloading mediapipe-1.1.1-py3-none-win_amd64.whl.metadata (10 kB)
Requirement already satisfied: numpy&gt;=2 in c:\programdata\anaconda3\lib\site-packages (from opencv-python) (2.3.5)
Collecting absl-py~=2.3 (from mediapipe)
  Downloading absl_py-2.5.1-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: certifi in c:\programdata\anaconda3\lib\site-packages (from mediapipe) (2025.11.12)
Collecting sounddevice~=0.5 (from mediapipe)
  Downloading sounddevice-0.5.6-py3-none-win_amd64.whl.metadata (1.4 kB)
Collecting flatbuffers~=25.9 (from mediapipe)
  Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
Collecting opencv-contrib-python (from mediapipe)
  Downloading opencv_contrib_python-5.0.0.93-cp37-abi3-win_amd64.whl.metadata (20 kB)
Requirement already satisfied: matplotlib in c:\programdata\anaconda3\lib\site-packages (from mediapipe) (3.10.6)
Requirement already satisfied: cffi in c:\programdata\anaconda3\lib\site-packages (from sounddevice~=0.5-&gt;mediapipe) (2.0.0)
Requirement already satisfied: pycparser in c:\programdata\anaconda3\lib\site-packages (from cffi-&gt;sounddevice~=0.5-&gt;mediapipe) (2.23)
Requirement already satisfied: contourpy&gt;=1.0.1 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (1.3.3)
Requirement already satisfied: cycler&gt;=0.10 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (0.11.0)
Requirement already satisfied: fonttools&gt;=4.22.0 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (4.60.1)
Requirement already satisfied: kiwisolver&gt;=1.3.1 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (1.4.9)
Requirement already satisfied: packaging&gt;=20.0 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (25.0)
Requirement already satisfied: pillow&gt;=8 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (12.0.0)
Requirement already satisfied: pyparsing&gt;=2.3.1 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (3.2.5)
Requirement already satisfied: python-dateutil&gt;=2.7 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (2.9.0.post0)
Requirement already satisfied: six&gt;=1.5 in c:\programdata\anaconda3\lib\site-packages (from python-dateutil&gt;=2.7-&gt;matplotlib-&gt;mediapipe) (1.17.0)
Downloading opencv_python-5.0.0.93-cp37-abi3-win_amd64.whl (44.0 MB)
   ---------------------------------------- 0.0/44.0 MB ? eta -:--:--
    --------------------------------------- 0.8/44.0 MB 5.4 MB/s eta 0:00:08
   - -------------------------------------- 2.1/44.0 MB 6.3 MB/s eta 0:00:07
   --- ------------------------------------ 3.7/44.0 MB 6.5 MB/s eta 0:00:07
   ---- ----------------------------------- 5.0/44.0 MB 6.6 MB/s eta 0:00:06
   ----- ---------------------------------- 6.3/44.0 MB 6.6 MB/s eta 0:00:06
   ------- -------------------------------- 7.9/44.0 MB 6.7 MB/s eta 0:00:06
   -------- ------------------------------- 9.2/44.0 MB 6.8 MB/s eta 0:00:06
   --------- ------------------------------ 10.7/44.0 MB 6.8 MB/s eta 0:00:05
   ----------- ---------------------------- 12.3/44.0 MB 6.9 MB/s eta 0:00:05
   ------------ --------------------------- 13.9/44.0 MB 6.9 MB/s eta 0:00:05
   -------------- ------------------------- 15.5/44.0 MB 6.9 MB/s eta 0:00:05
   --------------- ------------------------ 16.8/44.0 MB 7.0 MB/s eta 0:00:04
   ---------------- ----------------------- 18.4/44.0 MB 7.0 MB/s eta 0:00:04
   ------------------ --------------------- 19.9/44.0 MB 7.0 MB/s eta 0:00:04
   ------------------- -------------------- 21.2/44.0 MB 7.0 MB/s eta 0:00:04
   -------------------- ------------------- 22.8/44.0 MB 7.0 MB/s eta 0:00:04
   --------------------- ------------------ 24.1/44.0 MB 7.0 MB/s eta 0:00:03
   ----------------------- ---------------- 25.7/44.0 MB 7.0 MB/s eta 0:00:03
   ------------------------ --------------- 27.3/44.0 MB 7.0 MB/s eta 0:00:03
   -------------------------- ------------- 28.8/44.0 MB 7.1 MB/s eta 0:00:03
   --------------------------- ------------ 30.4/44.0 MB 7.1 MB/s eta 0:00:02
   ---------------------------- ----------- 31.7/44.0 MB 7.1 MB/s eta 0:00:02
   ------------------------------ --------- 33.3/44.0 MB 7.1 MB/s eta 0:00:02
   ------------------------------- -------- 34.9/44.0 MB 7.1 MB/s eta 0:00:02
   -------------------------------- ------- 36.2/44.0 MB 7.1 MB/s eta 0:00:02
   ---------------------------------- ----- 37.5/44.0 MB 7.1 MB/s eta 0:00:01
   ----------------------------------- ---- 39.1/44.0 MB 7.0 MB/s eta 0:00:01
   ------------------------------------ --- 40.4/44.0 MB 7.0 MB/s eta 0:00:01
   -------------------------------------- - 41.9/44.0 MB 7.0 MB/s eta 0:00:01
   ---------------------------------------  43.3/44.0 MB 7.0 MB/s eta 0:00:01
   ---------------------------------------  43.8/44.0 MB 7.0 MB/s eta 0:00:01
   ---------------------------------------- 44.0/44.0 MB 6.8 MB/s  0:00:06
Downloading mediapipe-1.1.1-py3-none-win_amd64.whl (22.8 MB)
   ---------------------------------------- 0.0/22.8 MB ? eta -:--:--
   -- ------------------------------------- 1.3/22.8 MB 6.9 MB/s eta 0:00:04
   ----- ---------------------------------- 2.9/22.8 MB 7.1 MB/s eta 0:00:03
   ------- -------------------------------- 4.2/22.8 MB 6.9 MB/s eta 0:00:03
   --------- ------------------------------ 5.2/22.8 MB 6.9 MB/s eta 0:00:03
   ----------- ---------------------------- 6.8/22.8 MB 6.7 MB/s eta 0:00:03
   -------------- ------------------------- 8.4/22.8 MB 6.8 MB/s eta 0:00:03
   ----------------- ---------------------- 9.7/22.8 MB 6.8 MB/s eta 0:00:02
   ------------------- -------------------- 11.3/22.8 MB 6.9 MB/s eta 0:00:02
   ---------------------- ----------------- 12.8/22.8 MB 6.9 MB/s eta 0:00:02
   ------------------------ --------------- 14.2/22.8 MB 6.9 MB/s eta 0:00:02
   --------------------------- ------------ 15.7/22.8 MB 7.0 MB/s eta 0:00:02
   --------------------------- ------------ 15.7/22.8 MB 7.0 MB/s eta 0:00:02
   ----------------------------- ---------- 16.8/22.8 MB 6.2 MB/s eta 0:00:01
   -------------------------------- ------- 18.4/22.8 MB 6.3 MB/s eta 0:00:01
   ---------------------------------- ----- 19.7/22.8 MB 6.4 MB/s eta 0:00:01
   ------------------------------------- -- 21.2/22.8 MB 6.4 MB/s eta 0:00:01
   ---------------------------------------  22.5/22.8 MB 6.5 MB/s eta 0:00:01
   ---------------------------------------- 22.8/22.8 MB 6.3 MB/s  0:00:03
Downloading absl_py-2.5.1-py3-none-any.whl (137 kB)
Downloading flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)
Downloading sounddevice-0.5.6-py3-none-win_amd64.whl (1.0 MB)
   ---------------------------------------- 0.0/1.0 MB ? eta -:--:--
   ---------------------------------------- 1.0/1.0 MB 6.2 MB/s  0:00:00
Downloading opencv_contrib_python-5.0.0.93-cp37-abi3-win_amd64.whl (53.8 MB)
   ---------------------------------------- 0.0/53.8 MB ? eta -:--:--
   - -------------------------------------- 1.6/53.8 MB 7.3 MB/s eta 0:00:08
   -- ------------------------------------- 2.9/53.8 MB 7.2 MB/s eta 0:00:08
   --- ------------------------------------ 4.5/53.8 MB 7.3 MB/s eta 0:00:07
   ---- ----------------------------------- 6.0/53.8 MB 7.3 MB/s eta 0:00:07
   ----- ---------------------------------- 7.6/53.8 MB 7.3 MB/s eta 0:00:07
   ------ --------------------------------- 8.9/53.8 MB 7.3 MB/s eta 0:00:07
   ------- -------------------------------- 10.5/53.8 MB 7.3 MB/s eta 0:00:06
   -------- ------------------------------- 12.1/53.8 MB 7.3 MB/s eta 0:00:06
   ---------- ----------------------------- 13.6/53.8 MB 7.3 MB/s eta 0:00:06
   ----------- ---------------------------- 14.9/53.8 MB 7.2 MB/s eta 0:00:06
   ------------ --------------------------- 16.5/53.8 MB 7.2 MB/s eta 0:00:06
   ------------- -------------------------- 18.1/53.8 MB 7.2 MB/s eta 0:00:05
   -------------- ------------------------- 19.7/53.8 MB 7.3 MB/s eta 0:00:05
   --------------- ------------------------ 21.2/53.8 MB 7.3 MB/s eta 0:00:05
   ---------------- ----------------------- 22.8/53.8 MB 7.2 MB/s eta 0:00:05
   ------------------ --------------------- 24.4/53.8 MB 7.3 MB/s eta 0:00:05
   ------------------- -------------------- 25.7/53.8 MB 7.3 MB/s eta 0:00:04
   -------------------- ------------------- 27.3/53.8 MB 7.3 MB/s eta 0:00:04
   --------------------- ------------------ 28.8/53.8 MB 7.2 MB/s eta 0:00:04
   ---------------------- ----------------- 30.4/53.8 MB 7.3 MB/s eta 0:00:04
   ----------------------- ---------------- 31.7/53.8 MB 7.2 MB/s eta 0:00:04
   ------------------------ --------------- 33.3/53.8 MB 7.2 MB/s eta 0:00:03
   ------------------------- -------------- 34.9/53.8 MB 7.2 MB/s eta 0:00:03
   --------------------------- ------------ 36.4/53.8 MB 7.2 MB/s eta 0:00:03
   ---------------------------- ----------- 38.0/53.8 MB 7.2 MB/s eta 0:00:03
   ----------------------------- ---------- 39.3/53.8 MB 7.2 MB/s eta 0:00:03
   ------------------------------ --------- 40.9/53.8 MB 7.2 MB/s eta 0:00:02
   ------------------------------- -------- 42.5/53.8 MB 7.2 MB/s eta 0:00:02
   -------------------------------- ------- 44.0/53.8 MB 7.2 MB/s eta 0:00:02
   --------------------------------- ------ 45.6/53.8 MB 7.2 MB/s eta 0:00:02
   ----------------------------------- ---- 47.2/53.8 MB 7.2 MB/s eta 0:00:01
   ------------------------------------ --- 48.5/53.8 MB 7.2 MB/s eta 0:00:01
   ------------------------------------- -- 50.1/53.8 MB 7.2 MB/s eta 0:00:01
   -------------------------------------- - 51.6/53.8 MB 7.2 MB/s eta 0:00:01
   ---------------------------------------  53.0/53.8 MB 7.2 MB/s eta 0:00:01
   ---------------------------------------  53.7/53.8 MB 7.2 MB/s eta 0:00:01
   ---------------------------------------- 53.8/53.8 MB 7.0 MB/s  0:00:07
Installing collected packages: flatbuffers, opencv-python, opencv-contrib-python, absl-py, sounddevice, mediapipe

   ---------------------------------------- 0/6 [flatbuffers]
   ---------------------------------------- 0/6 [flatbuffers]
   ------ --------------------------------- 1/6 [opencv-python]
   ------ --------------------------------- 1/6 [opencv-python]
   ------ --------------------------------- 1/6 [opencv-python]
   ------ --------------------------------- 1/6 [opencv-python]
   ------ --------------------------------- 1/6 [opencv-python]
   ------ --------------------------------- 1/6 [opencv-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   ------------- -------------------------- 2/6 [opencv-contrib-python]
   -------------------- ------------------- 3/6 [absl-py]
   -------------------- ------------------- 3/6 [absl-py]
   -------------------- ------------------- 3/6 [absl-py]
   -------------------- ------------------- 3/6 [absl-py]
   -------------------- ------------------- 3/6 [absl-py]
   -------------------- ------------------- 3/6 [absl-py]
   -------------------------- ------------- 4/6 [sounddevice]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   --------------------------------- ------ 5/6 [mediapipe]
   ---------------------------------------- 6/6 [mediapipe]

Successfully installed absl-py-2.5.1 flatbuffers-25.12.19 mediapipe-1.1.1 opencv-contrib-python-5.0.0.93 opencv-python-5.0.0.93 sounddevice-0.5.6
Note: you may need to restart the kernel to use updated packages.
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=60ab96e7-0209-485d-b1f3-de4dd7d72523">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">sys</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Python executable:"</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Python version:"</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">)</span>
<span class="o">%</span><span class="k">pip</span> --version
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Python executable: C:\ProgramData\anaconda3\python.exe
Python version: 3.13.9 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 19:09:58) [MSC v.1929 64 bit (AMD64)]
pip 25.3 from C:\ProgramData\anaconda3\Lib\site-packages\pip (python 3.13)

Note: you may need to restart the kernel to use updated packages.
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=5c677e54-2faa-4349-9c71-9fbb7db29ab5">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">pip</span> install opencv-python
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: opencv-python in c:\users\alisha p\appdata\roaming\python\python313\site-packages (5.0.0.93)
Requirement already satisfied: numpy&gt;=2 in c:\programdata\anaconda3\lib\site-packages (from opencv-python) (2.3.5)
Note: you may need to restart the kernel to use updated packages.
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=db8da6ea-c571-44c7-9c21-1b29b38ab38a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">cv2</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"OpenCV version:"</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Zenvia camera module ready!"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>OpenCV version: 5.0.0
Zenvia camera module ready!
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=b3f4f44a-b3e4-4a40-817a-c854ae5d7c08">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [3]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">cv2</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">IPython.display</span><span class="w"> </span><span class="kn">import</span> <span class="n">display</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">PIL</span><span class="w"> </span><span class="kn">import</span> <span class="n">Image</span>

<span class="n">cap</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">VideoCapture</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="k">if</span> <span class="n">cap</span><span class="o">.</span><span class="n">isOpened</span><span class="p">():</span>
    <span class="n">ret</span><span class="p">,</span> <span class="n">frame</span> <span class="o">=</span> <span class="n">cap</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

    <span class="k">if</span> <span class="n">ret</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Zenvia camera test: SUCCESS"</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Frame size:"</span><span class="p">,</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
        <span class="n">frame</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">frame</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2RGB</span><span class="p">)</span>
        <span class="n">display</span><span class="p">(</span><span class="n">Image</span><span class="o">.</span><span class="n">fromarray</span><span class="p">(</span><span class="n">frame</span><span class="p">))</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Camera opened, but no frame received."</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Camera unavailable. Check permissions or camera index."</span><span class="p">)</span>

<span class="n">cap</span><span class="o">.</span><span class="n">release</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Zenvia camera test: SUCCESS
Frame size: (480, 640, 3)
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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"/>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=203e443f-56eb-49ae-8c6d-0c23da3ac1b3">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [4]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">pip</span> install mediapipe
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: mediapipe in c:\users\alisha p\appdata\roaming\python\python313\site-packages (1.1.1)
Requirement already satisfied: absl-py~=2.3 in c:\users\alisha p\appdata\roaming\python\python313\site-packages (from mediapipe) (2.5.1)
Requirement already satisfied: certifi in c:\programdata\anaconda3\lib\site-packages (from mediapipe) (2025.11.12)
Requirement already satisfied: numpy in c:\programdata\anaconda3\lib\site-packages (from mediapipe) (2.3.5)
Requirement already satisfied: sounddevice~=0.5 in c:\users\alisha p\appdata\roaming\python\python313\site-packages (from mediapipe) (0.5.6)
Requirement already satisfied: flatbuffers~=25.9 in c:\users\alisha p\appdata\roaming\python\python313\site-packages (from mediapipe) (25.12.19)
Requirement already satisfied: opencv-contrib-python in c:\users\alisha p\appdata\roaming\python\python313\site-packages (from mediapipe) (5.0.0.93)
Requirement already satisfied: matplotlib in c:\programdata\anaconda3\lib\site-packages (from mediapipe) (3.10.6)
Requirement already satisfied: cffi in c:\programdata\anaconda3\lib\site-packages (from sounddevice~=0.5-&gt;mediapipe) (2.0.0)
Requirement already satisfied: pycparser in c:\programdata\anaconda3\lib\site-packages (from cffi-&gt;sounddevice~=0.5-&gt;mediapipe) (2.23)
Requirement already satisfied: contourpy&gt;=1.0.1 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (1.3.3)
Requirement already satisfied: cycler&gt;=0.10 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (0.11.0)
Requirement already satisfied: fonttools&gt;=4.22.0 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (4.60.1)
Requirement already satisfied: kiwisolver&gt;=1.3.1 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (1.4.9)
Requirement already satisfied: packaging&gt;=20.0 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (25.0)
Requirement already satisfied: pillow&gt;=8 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (12.0.0)
Requirement already satisfied: pyparsing&gt;=2.3.1 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (3.2.5)
Requirement already satisfied: python-dateutil&gt;=2.7 in c:\programdata\anaconda3\lib\site-packages (from matplotlib-&gt;mediapipe) (2.9.0.post0)
Requirement already satisfied: six&gt;=1.5 in c:\programdata\anaconda3\lib\site-packages (from python-dateutil&gt;=2.7-&gt;matplotlib-&gt;mediapipe) (1.17.0)
Note: you may need to restart the kernel to use updated packages.
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=ce5c0deb-e682-4da0-a2dc-e25478f967d6">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [5]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">cv2</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">mediapipe</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mp</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"OpenCV:"</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"MediaPipe:"</span><span class="p">,</span> <span class="n">mp</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Zenvia gesture recognition modules ready!"</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>OpenCV: 5.0.0
MediaPipe: 1.1.1
Zenvia gesture recognition modules ready!
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=263508df-64ae-4227-9727-8c1a80457ee1">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [9]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">mediapipe</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mp</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"MediaPipe version:"</span><span class="p">,</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">mp</span><span class="p">,</span> <span class="s2">"__version__"</span><span class="p">,</span> <span class="s2">"Unknown"</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"MediaPipe location:"</span><span class="p">,</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">mp</span><span class="p">,</span> <span class="s2">"__file__"</span><span class="p">,</span> <span class="s2">"Unknown"</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Python location:"</span><span class="p">,</span> <span class="n">sys</span><span class="o">.</span><span class="n">executable</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Has solutions:"</span><span class="p">,</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">mp</span><span class="p">,</span> <span class="s2">"solutions"</span><span class="p">))</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>MediaPipe version: 1.1.1
MediaPipe location: C:\Users\ALISHA P\AppData\Roaming\Python\Python313\site-packages\mediapipe\__init__.py
Python location: C:\ProgramData\anaconda3\python.exe
Has solutions: False
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=b77ba756-2926-488d-96ed-a2bb7645dd24">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [10]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">pip</span> install --force-reinstall mediapipe==0.10.21
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Defaulting to user installation because normal site-packages is not writeable
Note: you may need to restart the kernel to use updated packages.
</pre>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>ERROR: Could not find a version that satisfies the requirement mediapipe==0.10.21 (from versions: 0.10.30, 0.10.31, 0.10.32, 0.10.33, 0.10.35, 1.0.0, 1.0.1, 1.1.0, 1.1.1)
ERROR: No matching distribution found for mediapipe==0.10.21
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=f2533986-b2a9-4cce-9ebe-8f0a0e314b57">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [11]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">mediapipe</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mp</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"MediaPipe version:"</span><span class="p">,</span> <span class="n">mp</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>

<span class="k">try</span><span class="p">:</span>
    <span class="kn">from</span><span class="w"> </span><span class="nn">mediapipe.tasks.python</span><span class="w"> </span><span class="kn">import</span> <span class="n">vision</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Tasks API available!"</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Tasks API error:"</span><span class="p">,</span> <span class="nb">repr</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>MediaPipe version: 1.1.1
Tasks API available!
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=e92497b6-6672-4a05-9093-9e1f16bad2da">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [16]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>C:\Users\ALISHA P
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=4662a22f-dafd-4b5b-94d1-c62948d7f34f">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [19]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">"hand_landmarker.task"</span><span class="p">))</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>False
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=daadf757-9748-492e-9d7c-57f7c04be64a">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [20]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>C:\Users\ALISHA P
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=c6463b9f-c287-47e4-8ae6-e389057cb3c6">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [21]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"Current folder:"</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Files in this folder:"</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">())</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Current folder: C:\Users\ALISHA P
Files in this folder: ['.anaconda', '.arduinoIDE', '.conda', '.condarc', '.continuum', '.copilot', '.gemini', '.ipynb_checkpoints', '.ipython', '.jupyter', '.matplotlib', '.ms-ad', '.vscode', '.vscode-shared', 'AppData', 'Application Data', 'bool', 'Contacts', 'converted_file.xlsx', 'Cookies', 'CrossDevice', 'Documents', 'Downloads', 'DSA.ipynb', 'Favorites', 'float', 'IDE Arduino', 'Links', 'lisha', 'Local Settings', 'ML.ipynb', 'My Documents', 'NetHood', 'NEWW', 'NTUSER.DAT', 'ntuser.dat.LOG1', 'ntuser.dat.LOG2', 'NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TM.blf', 'NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000001.regtrans-ms', 'NTUSER.DAT{2ad838bc-efea-11ee-a54d-000d3a94eaa1}.TMContainer00000000000000000002.regtrans-ms', 'ntuser.ini', 'OneDrive', 'Optional[Dict]', 'Optional[str]', 'PrintHood', 'PRogram.ipynb', 'Recent', 'Saved Games', 'Searches', 'SendTo', 'Start Menu', 'store_transactions.db', 'Templates', 'Untitled.ipynb', 'Untitled1.ipynb', 'webapp.ipynb', 'ZENVIA INDUS.ipynb']
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=95405758-444d-4763-809f-45a745467029">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [22]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">os</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">expanduser</span><span class="p">(</span><span class="s2">"~/Downloads/hand_landmarker.task"</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"File found in Downloads:"</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">file_path</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Full file path:"</span><span class="p">,</span> <span class="n">file_path</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>File found in Downloads: True
Full file path: C:\Users\ALISHA P/Downloads/hand_landmarker.task
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=21b4893a-cefc-40d4-82ca-510e08a70816">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [2]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">shutil</span>

<span class="n">source</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">expanduser</span><span class="p">(</span><span class="s2">"~/Downloads/hand_landmarker.task"</span><span class="p">)</span>
<span class="n">destination</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">(),</span> <span class="s2">"hand_landmarker.task"</span><span class="p">)</span>

<span class="n">shutil</span><span class="o">.</span><span class="n">copy2</span><span class="p">(</span><span class="n">source</span><span class="p">,</span> <span class="n">destination</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"File copied successfully!"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"File found in Jupyter folder:"</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">destination</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Destination:"</span><span class="p">,</span> <span class="n">destination</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>File copied successfully!
File found in Jupyter folder: True
Destination: C:\Users\ALISHA P\hand_landmarker.task
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=a9b5711c-6daf-48aa-956b-d53c50f9f5f2">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">cv2</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">mediapipe</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mp</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">time</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">mediapipe.tasks</span><span class="w"> </span><span class="kn">import</span> <span class="n">python</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">mediapipe.tasks.python</span><span class="w"> </span><span class="kn">import</span> <span class="n">vision</span>

<span class="n">model_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">(),</span> <span class="s2">"hand_landmarker.task"</span><span class="p">)</span>

<span class="n">options</span> <span class="o">=</span> <span class="n">vision</span><span class="o">.</span><span class="n">HandLandmarkerOptions</span><span class="p">(</span>
    <span class="n">base_options</span><span class="o">=</span><span class="n">python</span><span class="o">.</span><span class="n">BaseOptions</span><span class="p">(</span>
        <span class="n">model_asset_path</span><span class="o">=</span><span class="n">model_path</span>
    <span class="p">),</span>
    <span class="n">running_mode</span><span class="o">=</span><span class="n">vision</span><span class="o">.</span><span class="n">RunningMode</span><span class="o">.</span><span class="n">VIDEO</span><span class="p">,</span>
    <span class="n">num_hands</span><span class="o">=</span><span class="mi">1</span>
<span class="p">)</span>

<span class="n">cap</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">VideoCapture</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="k">with</span> <span class="n">vision</span><span class="o">.</span><span class="n">HandLandmarker</span><span class="o">.</span><span class="n">create_from_options</span><span class="p">(</span><span class="n">options</span><span class="p">)</span> <span class="k">as</span> <span class="n">detector</span><span class="p">:</span>
    <span class="k">while</span> <span class="n">cap</span><span class="o">.</span><span class="n">isOpened</span><span class="p">():</span>
        <span class="n">success</span><span class="p">,</span> <span class="n">frame</span> <span class="o">=</span> <span class="n">cap</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">success</span><span class="p">:</span>
            <span class="k">break</span>

        <span class="n">frame</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">flip</span><span class="p">(</span><span class="n">frame</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
        <span class="n">rgb</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">frame</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2RGB</span><span class="p">)</span>

        <span class="n">image</span> <span class="o">=</span> <span class="n">mp</span><span class="o">.</span><span class="n">Image</span><span class="p">(</span>
            <span class="n">image_format</span><span class="o">=</span><span class="n">mp</span><span class="o">.</span><span class="n">ImageFormat</span><span class="o">.</span><span class="n">SRGB</span><span class="p">,</span>
            <span class="n">data</span><span class="o">=</span><span class="n">rgb</span>
        <span class="p">)</span>

        <span class="n">timestamp</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">monotonic</span><span class="p">()</span> <span class="o">*</span> <span class="mi">1000</span><span class="p">)</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">detector</span><span class="o">.</span><span class="n">detect_for_video</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">timestamp</span><span class="p">)</span>

        <span class="n">message</span> <span class="o">=</span> <span class="s2">"Show your open palm"</span>
        <span class="n">color</span> <span class="o">=</span> <span class="p">(</span><span class="mi">255</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">255</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">result</span><span class="o">.</span><span class="n">hand_landmarks</span><span class="p">:</span>
            <span class="n">hand</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">hand_landmarks</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

            <span class="c1"># Check whether each finger is extended</span>
            <span class="n">index_up</span> <span class="o">=</span> <span class="n">hand</span><span class="p">[</span><span class="mi">8</span><span class="p">]</span><span class="o">.</span><span class="n">y</span> <span class="o">&lt;</span> <span class="n">hand</span><span class="p">[</span><span class="mi">6</span><span class="p">]</span><span class="o">.</span><span class="n">y</span>
            <span class="n">middle_up</span> <span class="o">=</span> <span class="n">hand</span><span class="p">[</span><span class="mi">12</span><span class="p">]</span><span class="o">.</span><span class="n">y</span> <span class="o">&lt;</span> <span class="n">hand</span><span class="p">[</span><span class="mi">10</span><span class="p">]</span><span class="o">.</span><span class="n">y</span>
            <span class="n">ring_up</span> <span class="o">=</span> <span class="n">hand</span><span class="p">[</span><span class="mi">16</span><span class="p">]</span><span class="o">.</span><span class="n">y</span> <span class="o">&lt;</span> <span class="n">hand</span><span class="p">[</span><span class="mi">14</span><span class="p">]</span><span class="o">.</span><span class="n">y</span>
            <span class="n">little_up</span> <span class="o">=</span> <span class="n">hand</span><span class="p">[</span><span class="mi">20</span><span class="p">]</span><span class="o">.</span><span class="n">y</span> <span class="o">&lt;</span> <span class="n">hand</span><span class="p">[</span><span class="mi">18</span><span class="p">]</span><span class="o">.</span><span class="n">y</span>

            <span class="c1"># Thumb extends sideways in the mirrored camera view</span>
            <span class="n">thumb_up</span> <span class="o">=</span> <span class="nb">abs</span><span class="p">(</span><span class="n">hand</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span><span class="o">.</span><span class="n">x</span> <span class="o">-</span> <span class="n">hand</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">x</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mf">0.04</span>

            <span class="k">if</span> <span class="n">index_up</span> <span class="ow">and</span> <span class="n">middle_up</span> <span class="ow">and</span> <span class="n">ring_up</span> <span class="ow">and</span> <span class="n">little_up</span> <span class="ow">and</span> <span class="n">thumb_up</span><span class="p">:</span>
                <span class="n">message</span> <span class="o">=</span> <span class="s2">"STOP GESTURE DETECTED"</span>
                <span class="n">color</span> <span class="o">=</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">message</span> <span class="o">=</span> <span class="s2">"HAND DETECTED"</span>
                <span class="n">color</span> <span class="o">=</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>

            <span class="k">for</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">hand</span><span class="p">:</span>
                <span class="n">x</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">point</span><span class="o">.</span><span class="n">x</span> <span class="o">*</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
                <span class="n">y</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">point</span><span class="o">.</span><span class="n">y</span> <span class="o">*</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
                <span class="n">cv2</span><span class="o">.</span><span class="n">circle</span><span class="p">(</span><span class="n">frame</span><span class="p">,</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">),</span> <span class="mi">4</span><span class="p">,</span> <span class="n">color</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>

        <span class="n">cv2</span><span class="o">.</span><span class="n">putText</span><span class="p">(</span>
            <span class="n">frame</span><span class="p">,</span> <span class="n">message</span><span class="p">,</span> <span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">40</span><span class="p">),</span>
            <span class="n">cv2</span><span class="o">.</span><span class="n">FONT_HERSHEY_SIMPLEX</span><span class="p">,</span> <span class="mf">0.8</span><span class="p">,</span> <span class="n">color</span><span class="p">,</span> <span class="mi">2</span>
        <span class="p">)</span>

        <span class="n">cv2</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="s2">"Zenvia - STOP Gesture Test"</span><span class="p">,</span> <span class="n">frame</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">cv2</span><span class="o">.</span><span class="n">waitKey</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mh">0xFF</span> <span class="o">==</span> <span class="nb">ord</span><span class="p">(</span><span class="s2">"q"</span><span class="p">):</span>
            <span class="k">break</span>

<span class="n">cap</span><span class="o">.</span><span class="n">release</span><span class="p">()</span>
<span class="n">cv2</span><span class="o">.</span><span class="n">destroyAllWindows</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=773d5a8d-931b-466d-85cb-da9f234dbe7d">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [8]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">pip</span> install paho-mqtt
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Defaulting to user installation because normal site-packages is not writeable
Collecting paho-mqtt
  Downloading paho_mqtt-2.1.0-py3-none-any.whl.metadata (23 kB)
Downloading paho_mqtt-2.1.0-py3-none-any.whl (67 kB)
Installing collected packages: paho-mqtt
Successfully installed paho-mqtt-2.1.0
Note: you may need to restart the kernel to use updated packages.
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=a0d1012b-3a5e-406b-9225-c6cebf7fdc85">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [11]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">paho.mqtt.client</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mqtt</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">time</span>

<span class="n">broker</span> <span class="o">=</span> <span class="s2">"broker.hivemq.com"</span>
<span class="n">port</span> <span class="o">=</span> <span class="mi">1883</span>

<span class="n">client</span> <span class="o">=</span> <span class="n">mqtt</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span>
    <span class="n">callback_api_version</span><span class="o">=</span><span class="n">mqtt</span><span class="o">.</span><span class="n">CallbackAPIVersion</span><span class="o">.</span><span class="n">VERSION2</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">"zenvia_python_test_73821"</span>
<span class="p">)</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">client</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">broker</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span>
    <span class="n">client</span><span class="o">.</span><span class="n">loop_start</span><span class="p">()</span>
    <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">client</span><span class="o">.</span><span class="n">is_connected</span><span class="p">():</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"SUCCESS: Connected to MQTT broker!"</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"NOT CONNECTED: Check the network or broker."</span><span class="p">)</span>

    <span class="n">client</span><span class="o">.</span><span class="n">disconnect</span><span class="p">()</span>
    <span class="n">client</span><span class="o">.</span><span class="n">loop_stop</span><span class="p">()</span>

<span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Connection failed:"</span><span class="p">,</span> <span class="nb">repr</span><span class="p">(</span><span class="n">e</span><span class="p">))</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>SUCCESS: Connected to MQTT broker!
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=cb9e1d66-2a11-4f64-9d2b-947a7256ee62">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [12]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">paho.mqtt.client</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mqtt</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">time</span>

<span class="n">broker</span> <span class="o">=</span> <span class="s2">"broker.hivemq.com"</span>
<span class="n">port</span> <span class="o">=</span> <span class="mi">1883</span>
<span class="n">topic</span> <span class="o">=</span> <span class="s2">"zenvia/demo/gesture-73821"</span>

<span class="n">client</span> <span class="o">=</span> <span class="n">mqtt</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span>
    <span class="n">callback_api_version</span><span class="o">=</span><span class="n">mqtt</span><span class="o">.</span><span class="n">CallbackAPIVersion</span><span class="o">.</span><span class="n">VERSION2</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">"zenvia_python_test_98462"</span>
<span class="p">)</span>

<span class="n">client</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">broker</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span>
<span class="n">client</span><span class="o">.</span><span class="n">loop_start</span><span class="p">()</span>

<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="n">info</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">publish</span><span class="p">(</span><span class="n">topic</span><span class="p">,</span> <span class="s2">"STOP"</span><span class="p">)</span>
<span class="n">info</span><span class="o">.</span><span class="n">wait_for_publish</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"Publish result:"</span><span class="p">,</span> <span class="n">info</span><span class="o">.</span><span class="n">rc</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Message sent:"</span><span class="p">,</span> <span class="n">info</span><span class="o">.</span><span class="n">is_published</span><span class="p">())</span>

<span class="n">client</span><span class="o">.</span><span class="n">disconnect</span><span class="p">()</span>
<span class="n">client</span><span class="o">.</span><span class="n">loop_stop</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Publish result: 0
Message sent: True
</pre>
</div>
</div>
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[12]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>&lt;MQTTErrorCode.MQTT_ERR_SUCCESS: 0&gt;</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=9f0cb0b2-7814-4624-9478-3a2b1bd8ed20">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [9]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">paho.mqtt.client</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mqtt</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">time</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">uuid</span>

<span class="n">broker</span> <span class="o">=</span> <span class="s2">"broker.hivemq.com"</span>
<span class="n">port</span> <span class="o">=</span> <span class="mi">1883</span>
<span class="n">topic</span> <span class="o">=</span> <span class="s2">"zenvia/demo/gesture-73821"</span>

<span class="n">client</span> <span class="o">=</span> <span class="n">mqtt</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span>
    <span class="n">callback_api_version</span><span class="o">=</span><span class="n">mqtt</span><span class="o">.</span><span class="n">CallbackAPIVersion</span><span class="o">.</span><span class="n">VERSION2</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">"zenvia-test-"</span> <span class="o">+</span> <span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()</span><span class="o">.</span><span class="n">hex</span><span class="p">[:</span><span class="mi">8</span><span class="p">]</span>
<span class="p">)</span>

<span class="n">client</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">broker</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span>
<span class="n">client</span><span class="o">.</span><span class="n">loop_start</span><span class="p">()</span>

<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">publish</span><span class="p">(</span><span class="n">topic</span><span class="p">,</span> <span class="s2">"STOP"</span><span class="p">)</span>
<span class="n">result</span><span class="o">.</span><span class="n">wait_for_publish</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"Topic:"</span><span class="p">,</span> <span class="n">topic</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Publish status:"</span><span class="p">,</span> <span class="n">result</span><span class="o">.</span><span class="n">rc</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Published:"</span><span class="p">,</span> <span class="n">result</span><span class="o">.</span><span class="n">is_published</span><span class="p">())</span>

<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="n">client</span><span class="o">.</span><span class="n">disconnect</span><span class="p">()</span>
<span class="n">client</span><span class="o">.</span><span class="n">loop_stop</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Topic: zenvia/demo/gesture-73821
Publish status: 0
Published: True
</pre>
</div>
</div>
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[9]:</div>
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>&lt;MQTTErrorCode.MQTT_ERR_SUCCESS: 0&gt;</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=4e64cff1-a955-492d-872a-c68fac74e035">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">cv2</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">mediapipe</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mp</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">time</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">math</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">uuid</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">paho.mqtt.client</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">mqtt</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">mediapipe.tasks</span><span class="w"> </span><span class="kn">import</span> <span class="n">python</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">mediapipe.tasks.python</span><span class="w"> </span><span class="kn">import</span> <span class="n">vision</span>

<span class="c1"># ---------- MQTT ----------</span>
<span class="n">BROKER</span> <span class="o">=</span> <span class="s2">"broker.hivemq.com"</span>
<span class="n">PORT</span> <span class="o">=</span> <span class="mi">1883</span>
<span class="n">TOPIC</span> <span class="o">=</span> <span class="s2">"zenvia/demo/gesture-73821"</span>

<span class="n">client</span> <span class="o">=</span> <span class="n">mqtt</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span>
    <span class="n">callback_api_version</span><span class="o">=</span><span class="n">mqtt</span><span class="o">.</span><span class="n">CallbackAPIVersion</span><span class="o">.</span><span class="n">VERSION2</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">"zenvia-control-"</span> <span class="o">+</span> <span class="n">uuid</span><span class="o">.</span><span class="n">uuid4</span><span class="p">()</span><span class="o">.</span><span class="n">hex</span><span class="p">[:</span><span class="mi">8</span><span class="p">]</span>
<span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"Connecting to MQTT..."</span><span class="p">)</span>
<span class="n">client</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">BROKER</span><span class="p">,</span> <span class="n">PORT</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span>
<span class="n">client</span><span class="o">.</span><span class="n">loop_start</span><span class="p">()</span>

<span class="c1"># Allow extra time for the MQTT connection</span>
<span class="k">for</span> <span class="n">attempt</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">client</span><span class="o">.</span><span class="n">is_connected</span><span class="p">():</span>
        <span class="k">break</span>
    <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>

<span class="k">if</span> <span class="n">client</span><span class="o">.</span><span class="n">is_connected</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"MQTT connected!"</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"MQTT connection failed after 10 seconds."</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Check your internet connection and MQTT broker availability."</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Do not start gesture detection until MQTT connects."</span><span class="p">)</span>


<span class="c1"># ---------- Hand model ----------</span>
<span class="n">model_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">(),</span> <span class="s2">"hand_landmarker.task"</span><span class="p">)</span>

<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">model_path</span><span class="p">):</span>
    <span class="n">client</span><span class="o">.</span><span class="n">loop_stop</span><span class="p">()</span>
    <span class="n">client</span><span class="o">.</span><span class="n">disconnect</span><span class="p">()</span>
    <span class="k">raise</span> <span class="ne">FileNotFoundError</span><span class="p">(</span><span class="s2">"hand_landmarker.task was not found!"</span><span class="p">)</span>

<span class="n">options</span> <span class="o">=</span> <span class="n">vision</span><span class="o">.</span><span class="n">HandLandmarkerOptions</span><span class="p">(</span>
    <span class="n">base_options</span><span class="o">=</span><span class="n">python</span><span class="o">.</span><span class="n">BaseOptions</span><span class="p">(</span>
        <span class="n">model_asset_path</span><span class="o">=</span><span class="n">model_path</span>
    <span class="p">),</span>
    <span class="n">running_mode</span><span class="o">=</span><span class="n">vision</span><span class="o">.</span><span class="n">RunningMode</span><span class="o">.</span><span class="n">VIDEO</span><span class="p">,</span>
    <span class="n">num_hands</span><span class="o">=</span><span class="mi">1</span>
<span class="p">)</span>

<span class="n">cap</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">VideoCapture</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="k">if</span> <span class="ow">not</span> <span class="n">cap</span><span class="o">.</span><span class="n">isOpened</span><span class="p">():</span>
    <span class="n">client</span><span class="o">.</span><span class="n">loop_stop</span><span class="p">()</span>
    <span class="n">client</span><span class="o">.</span><span class="n">disconnect</span><span class="p">()</span>
    <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s2">"Could not open webcam."</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">dist</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">math</span><span class="o">.</span><span class="n">hypot</span><span class="p">(</span><span class="n">a</span><span class="o">.</span><span class="n">x</span> <span class="o">-</span> <span class="n">b</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">a</span><span class="o">.</span><span class="n">y</span> <span class="o">-</span> <span class="n">b</span><span class="o">.</span><span class="n">y</span><span class="p">)</span>

<span class="k">def</span><span class="w"> </span><span class="nf">classify_gesture</span><span class="p">(</span><span class="n">hand</span><span class="p">):</span>
    <span class="c1"># Use palm size to normalize the thumb measurements.</span>
    <span class="n">palm_size</span> <span class="o">=</span> <span class="n">dist</span><span class="p">(</span><span class="n">hand</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">hand</span><span class="p">[</span><span class="mi">9</span><span class="p">])</span>
    <span class="k">if</span> <span class="n">palm_size</span> <span class="o">&lt;</span> <span class="mf">0.001</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"UNKNOWN"</span>

    <span class="c1"># Open palm: four fingers extended.</span>
    <span class="n">fingers_up</span> <span class="o">=</span> <span class="nb">all</span><span class="p">(</span>
        <span class="n">dist</span><span class="p">(</span><span class="n">hand</span><span class="p">[</span><span class="n">tip</span><span class="p">],</span> <span class="n">hand</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">&gt;</span> <span class="n">dist</span><span class="p">(</span><span class="n">hand</span><span class="p">[</span><span class="n">pip</span><span class="p">],</span> <span class="n">hand</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        <span class="k">for</span> <span class="n">tip</span><span class="p">,</span> <span class="n">pip</span> <span class="ow">in</span> <span class="p">[(</span><span class="mi">8</span><span class="p">,</span> <span class="mi">6</span><span class="p">),</span> <span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> <span class="p">(</span><span class="mi">16</span><span class="p">,</span> <span class="mi">14</span><span class="p">),</span> <span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">18</span><span class="p">)]</span>
    <span class="p">)</span>

    <span class="n">thumb_open</span> <span class="o">=</span> <span class="n">dist</span><span class="p">(</span><span class="n">hand</span><span class="p">[</span><span class="mi">4</span><span class="p">],</span> <span class="n">hand</span><span class="p">[</span><span class="mi">5</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mf">0.35</span> <span class="o">*</span> <span class="n">palm_size</span>

    <span class="k">if</span> <span class="n">fingers_up</span> <span class="ow">and</span> <span class="n">thumb_open</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"STOP"</span>

    <span class="c1"># Fist: four fingertips folded toward the wrist.</span>
    <span class="n">fingers_folded</span> <span class="o">=</span> <span class="nb">all</span><span class="p">(</span>
        <span class="n">dist</span><span class="p">(</span><span class="n">hand</span><span class="p">[</span><span class="n">tip</span><span class="p">],</span> <span class="n">hand</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">&lt;</span> <span class="n">dist</span><span class="p">(</span><span class="n">hand</span><span class="p">[</span><span class="n">pip</span><span class="p">],</span> <span class="n">hand</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        <span class="k">for</span> <span class="n">tip</span><span class="p">,</span> <span class="n">pip</span> <span class="ow">in</span> <span class="p">[(</span><span class="mi">8</span><span class="p">,</span> <span class="mi">6</span><span class="p">),</span> <span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> <span class="p">(</span><span class="mi">16</span><span class="p">,</span> <span class="mi">14</span><span class="p">),</span> <span class="p">(</span><span class="mi">20</span><span class="p">,</span> <span class="mi">18</span><span class="p">)]</span>
    <span class="p">)</span>

    <span class="n">thumb_folded</span> <span class="o">=</span> <span class="n">dist</span><span class="p">(</span><span class="n">hand</span><span class="p">[</span><span class="mi">4</span><span class="p">],</span> <span class="n">hand</span><span class="p">[</span><span class="mi">9</span><span class="p">])</span> <span class="o">&lt;</span> <span class="mf">0.65</span> <span class="o">*</span> <span class="n">palm_size</span>

    <span class="k">if</span> <span class="n">fingers_folded</span> <span class="ow">and</span> <span class="n">thumb_folded</span><span class="p">:</span>
        <span class="k">return</span> <span class="s2">"RUN"</span>

    <span class="k">return</span> <span class="s2">"UNKNOWN"</span>

<span class="n">last_sent_gesture</span> <span class="o">=</span> <span class="kc">None</span>
<span class="n">candidate_gesture</span> <span class="o">=</span> <span class="kc">None</span>
<span class="n">candidate_since</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">gesture_stability</span> <span class="o">=</span> <span class="mf">0.5</span>  <span class="c1"># seconds</span>
<span class="n">last_publish_time</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">publish_cooldown</span> <span class="o">=</span> <span class="mf">2.0</span>

<span class="k">try</span><span class="p">:</span>
    <span class="k">with</span> <span class="n">vision</span><span class="o">.</span><span class="n">HandLandmarker</span><span class="o">.</span><span class="n">create_from_options</span><span class="p">(</span><span class="n">options</span><span class="p">)</span> <span class="k">as</span> <span class="n">detector</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Zenvia gesture control started."</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Open palm = STOP | Closed fist = RUN request"</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Hold a gesture steady; press Q to exit."</span><span class="p">)</span>

        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
            <span class="n">success</span><span class="p">,</span> <span class="n">frame</span> <span class="o">=</span> <span class="n">cap</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">success</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="s2">"Could not read camera frame."</span><span class="p">)</span>
                <span class="k">break</span>

            <span class="n">frame</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">flip</span><span class="p">(</span><span class="n">frame</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
            <span class="n">rgb</span> <span class="o">=</span> <span class="n">cv2</span><span class="o">.</span><span class="n">cvtColor</span><span class="p">(</span><span class="n">frame</span><span class="p">,</span> <span class="n">cv2</span><span class="o">.</span><span class="n">COLOR_BGR2RGB</span><span class="p">)</span>

            <span class="n">mp_image</span> <span class="o">=</span> <span class="n">mp</span><span class="o">.</span><span class="n">Image</span><span class="p">(</span>
                <span class="n">image_format</span><span class="o">=</span><span class="n">mp</span><span class="o">.</span><span class="n">ImageFormat</span><span class="o">.</span><span class="n">SRGB</span><span class="p">,</span>
                <span class="n">data</span><span class="o">=</span><span class="n">rgb</span>
            <span class="p">)</span>

            <span class="n">timestamp_ms</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">monotonic</span><span class="p">()</span> <span class="o">*</span> <span class="mi">1000</span><span class="p">)</span>
            <span class="n">result</span> <span class="o">=</span> <span class="n">detector</span><span class="o">.</span><span class="n">detect_for_video</span><span class="p">(</span><span class="n">mp_image</span><span class="p">,</span> <span class="n">timestamp_ms</span><span class="p">)</span>

            <span class="n">detected</span> <span class="o">=</span> <span class="s2">"UNKNOWN"</span>

            <span class="k">if</span> <span class="n">result</span><span class="o">.</span><span class="n">hand_landmarks</span><span class="p">:</span>
                <span class="n">hand</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">hand_landmarks</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

                <span class="k">for</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">hand</span><span class="p">:</span>
                    <span class="n">x</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">point</span><span class="o">.</span><span class="n">x</span> <span class="o">*</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
                    <span class="n">y</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">point</span><span class="o">.</span><span class="n">y</span> <span class="o">*</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
                    <span class="n">cv2</span><span class="o">.</span><span class="n">circle</span><span class="p">(</span><span class="n">frame</span><span class="p">,</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">),</span> <span class="mi">4</span><span class="p">,</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>

                <span class="k">for</span> <span class="n">connection</span> <span class="ow">in</span> <span class="n">vision</span><span class="o">.</span><span class="n">HandLandmarksConnections</span><span class="o">.</span><span class="n">HAND_CONNECTIONS</span><span class="p">:</span>
                    <span class="n">a</span> <span class="o">=</span> <span class="n">hand</span><span class="p">[</span><span class="n">connection</span><span class="o">.</span><span class="n">start</span><span class="p">]</span>
                    <span class="n">b</span> <span class="o">=</span> <span class="n">hand</span><span class="p">[</span><span class="n">connection</span><span class="o">.</span><span class="n">end</span><span class="p">]</span>
                    <span class="n">cv2</span><span class="o">.</span><span class="n">line</span><span class="p">(</span>
                        <span class="n">frame</span><span class="p">,</span>
                        <span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">a</span><span class="o">.</span><span class="n">x</span> <span class="o">*</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span> <span class="nb">int</span><span class="p">(</span><span class="n">a</span><span class="o">.</span><span class="n">y</span> <span class="o">*</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">])),</span>
                        <span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">b</span><span class="o">.</span><span class="n">x</span> <span class="o">*</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span> <span class="nb">int</span><span class="p">(</span><span class="n">b</span><span class="o">.</span><span class="n">y</span> <span class="o">*</span> <span class="n">frame</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">])),</span>
                        <span class="p">(</span><span class="mi">255</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span> <span class="mi">2</span>
                    <span class="p">)</span>

                <span class="n">detected</span> <span class="o">=</span> <span class="n">classify_gesture</span><span class="p">(</span><span class="n">hand</span><span class="p">)</span>

            <span class="n">now</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">monotonic</span><span class="p">()</span>

            <span class="k">if</span> <span class="n">detected</span> <span class="o">!=</span> <span class="n">candidate_gesture</span><span class="p">:</span>
                <span class="n">candidate_gesture</span> <span class="o">=</span> <span class="n">detected</span>
                <span class="n">candidate_since</span> <span class="o">=</span> <span class="n">now</span>

            <span class="n">stable</span> <span class="o">=</span> <span class="p">(</span>
                <span class="n">detected</span> <span class="ow">in</span> <span class="p">(</span><span class="s2">"STOP"</span><span class="p">,</span> <span class="s2">"RUN"</span><span class="p">)</span>
                <span class="ow">and</span> <span class="n">now</span> <span class="o">-</span> <span class="n">candidate_since</span> <span class="o">&gt;=</span> <span class="n">gesture_stability</span>
            <span class="p">)</span>

            <span class="k">if</span> <span class="n">stable</span><span class="p">:</span>
                <span class="n">label</span> <span class="o">=</span> <span class="p">(</span>
                    <span class="s2">"OPEN PALM: STOP"</span>
                    <span class="k">if</span> <span class="n">detected</span> <span class="o">==</span> <span class="s2">"STOP"</span>
                    <span class="k">else</span> <span class="s2">"FIST: RUN REQUEST"</span>
                <span class="p">)</span>
                <span class="n">color</span> <span class="o">=</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">)</span> <span class="k">if</span> <span class="n">detected</span> <span class="o">==</span> <span class="s2">"STOP"</span> <span class="k">else</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">200</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>

                <span class="n">cv2</span><span class="o">.</span><span class="n">putText</span><span class="p">(</span>
                    <span class="n">frame</span><span class="p">,</span> <span class="n">label</span><span class="p">,</span> <span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">40</span><span class="p">),</span>
                    <span class="n">cv2</span><span class="o">.</span><span class="n">FONT_HERSHEY_SIMPLEX</span><span class="p">,</span> <span class="mf">0.7</span><span class="p">,</span> <span class="n">color</span><span class="p">,</span> <span class="mi">2</span>
                <span class="p">)</span>

                <span class="c1"># Send only when switching to a new stable gesture.</span>
                <span class="k">if</span> <span class="p">(</span>
                    <span class="n">detected</span> <span class="o">!=</span> <span class="n">last_sent_gesture</span>
                    <span class="ow">and</span> <span class="n">now</span> <span class="o">-</span> <span class="n">last_publish_time</span> <span class="o">&gt;=</span> <span class="n">publish_cooldown</span>
                <span class="p">):</span>
                    <span class="n">info</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">publish</span><span class="p">(</span><span class="n">TOPIC</span><span class="p">,</span> <span class="n">detected</span><span class="p">,</span> <span class="n">qos</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>

                    <span class="k">if</span> <span class="n">info</span><span class="o">.</span><span class="n">rc</span> <span class="o">==</span> <span class="n">mqtt</span><span class="o">.</span><span class="n">MQTT_ERR_SUCCESS</span><span class="p">:</span>
                        <span class="nb">print</span><span class="p">(</span><span class="s2">"MQTT command sent:"</span><span class="p">,</span> <span class="n">detected</span><span class="p">)</span>
                        <span class="n">last_sent_gesture</span> <span class="o">=</span> <span class="n">detected</span>
                        <span class="n">last_publish_time</span> <span class="o">=</span> <span class="n">now</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="nb">print</span><span class="p">(</span><span class="s2">"MQTT publish failed:"</span><span class="p">,</span> <span class="n">info</span><span class="o">.</span><span class="n">rc</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">cv2</span><span class="o">.</span><span class="n">putText</span><span class="p">(</span>
                    <span class="n">frame</span><span class="p">,</span> <span class="s2">"Show open palm or closed fist"</span><span class="p">,</span>
                    <span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">40</span><span class="p">),</span> <span class="n">cv2</span><span class="o">.</span><span class="n">FONT_HERSHEY_SIMPLEX</span><span class="p">,</span>
                    <span class="mf">0.6</span><span class="p">,</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">255</span><span class="p">,</span> <span class="mi">255</span><span class="p">),</span> <span class="mi">2</span>
                <span class="p">)</span>

            <span class="c1"># Allow another command after returning to a neutral hand.</span>
            <span class="k">if</span> <span class="n">detected</span> <span class="o">==</span> <span class="s2">"UNKNOWN"</span><span class="p">:</span>
                <span class="n">last_sent_gesture</span> <span class="o">=</span> <span class="kc">None</span>

            <span class="n">cv2</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="s2">"Zenvia - Gesture Control"</span><span class="p">,</span> <span class="n">frame</span><span class="p">)</span>

            <span class="k">if</span> <span class="n">cv2</span><span class="o">.</span><span class="n">waitKey</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="o">&amp;</span> <span class="mh">0xFF</span> <span class="o">==</span> <span class="nb">ord</span><span class="p">(</span><span class="s2">"q"</span><span class="p">):</span>
                <span class="k">break</span>

<span class="k">finally</span><span class="p">:</span>
    <span class="n">cap</span><span class="o">.</span><span class="n">release</span><span class="p">()</span>
    <span class="n">cv2</span><span class="o">.</span><span class="n">destroyAllWindows</span><span class="p">()</span>
    <span class="n">client</span><span class="o">.</span><span class="n">loop_stop</span><span class="p">()</span>
    <span class="n">client</span><span class="o">.</span><span class="n">disconnect</span><span class="p">()</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Webcam and MQTT closed."</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Connecting to MQTT...
MQTT connected!
Zenvia gesture control started.
Open palm = STOP | Closed fist = RUN request
Hold a gesture steady; press Q to exit.
MQTT command sent: RUN
MQTT command sent: STOP
MQTT command sent: RUN
MQTT command sent: STOP
MQTT command sent: RUN
MQTT command sent: STOP
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=e89ec1aa-2468-42e3-9220-ed1c5e8bbfaa">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [21]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="o">%</span><span class="k">pip</span> install streamlit
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: streamlit in c:\programdata\anaconda3\lib\site-packages (1.51.0)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker&lt;2,&gt;=1.5.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools&lt;7,&gt;=4.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (5.5.1)
Requirement already satisfied: click&lt;9,&gt;=7.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (8.2.1)
Requirement already satisfied: numpy&lt;3,&gt;=1.23 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (2.3.5)
Requirement already satisfied: packaging&lt;26,&gt;=20 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (25.0)
Requirement already satisfied: pandas&lt;3,&gt;=1.4.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (2.3.3)
Requirement already satisfied: pillow&lt;13,&gt;=7.1.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (12.0.0)
Requirement already satisfied: protobuf&lt;7,&gt;=3.20 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (5.29.3)
Requirement already satisfied: pyarrow&lt;22,&gt;=7.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (21.0.0)
Requirement already satisfied: requests&lt;3,&gt;=2.27 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (2.32.5)
Requirement already satisfied: tenacity&lt;10,&gt;=8.1.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml&lt;2,&gt;=0.10.1 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions&lt;5,&gt;=4.4.0 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (4.15.0)
Requirement already satisfied: watchdog&lt;7,&gt;=2.1.5 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,&lt;4,&gt;=3.0.7 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (3.1.45)
Requirement already satisfied: tornado!=6.5.0,&lt;7,&gt;=6.0.3 in c:\programdata\anaconda3\lib\site-packages (from streamlit) (6.5.1)
Requirement already satisfied: jinja2 in c:\programdata\anaconda3\lib\site-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (3.1.6)
Requirement already satisfied: jsonschema&gt;=3.0 in c:\programdata\anaconda3\lib\site-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (4.25.0)
Requirement already satisfied: narwhals&gt;=1.14.2 in c:\programdata\anaconda3\lib\site-packages (from altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (2.7.0)
Requirement already satisfied: colorama in c:\programdata\anaconda3\lib\site-packages (from click&lt;9,&gt;=7.0-&gt;streamlit) (0.4.6)
Requirement already satisfied: gitdb&lt;5,&gt;=4.0.1 in c:\programdata\anaconda3\lib\site-packages (from gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (4.0.12)
Requirement already satisfied: smmap&lt;6,&gt;=3.0.1 in c:\programdata\anaconda3\lib\site-packages (from gitdb&lt;5,&gt;=4.0.1-&gt;gitpython!=3.1.19,&lt;4,&gt;=3.0.7-&gt;streamlit) (4.0.0)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\programdata\anaconda3\lib\site-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2.9.0.post0)
Requirement already satisfied: pytz&gt;=2020.1 in c:\programdata\anaconda3\lib\site-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: tzdata&gt;=2022.7 in c:\programdata\anaconda3\lib\site-packages (from pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (2025.2)
Requirement already satisfied: charset_normalizer&lt;4,&gt;=2 in c:\programdata\anaconda3\lib\site-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.4.4)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in c:\programdata\anaconda3\lib\site-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (3.11)
Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in c:\programdata\anaconda3\lib\site-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2.5.0)
Requirement already satisfied: certifi&gt;=2017.4.17 in c:\programdata\anaconda3\lib\site-packages (from requests&lt;3,&gt;=2.27-&gt;streamlit) (2025.11.12)
Requirement already satisfied: attrs&gt;=22.2.0 in c:\programdata\anaconda3\lib\site-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (25.4.0)
Requirement already satisfied: jsonschema-specifications&gt;=2023.03.6 in c:\programdata\anaconda3\lib\site-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (2025.9.1)
Requirement already satisfied: referencing&gt;=0.28.4 in c:\programdata\anaconda3\lib\site-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (0.37.0)
Requirement already satisfied: rpds-py&gt;=0.7.1 in c:\programdata\anaconda3\lib\site-packages (from jsonschema&gt;=3.0-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (0.28.0)
Requirement already satisfied: six&gt;=1.5 in c:\programdata\anaconda3\lib\site-packages (from python-dateutil&gt;=2.8.2-&gt;pandas&lt;3,&gt;=1.4.0-&gt;streamlit) (1.17.0)
Requirement already satisfied: MarkupSafe&gt;=2.0 in c:\programdata\anaconda3\lib\site-packages (from jinja2-&gt;altair!=5.4.0,!=5.4.1,&lt;6,&gt;=4.0-&gt;streamlit) (3.0.2)
Note: you may need to restart the kernel to use updated packages.
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=4e2ffb7a-8bdc-4d36-bece-0aea34006d19">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">streamlit</span><span class="w"> </span><span class="k">as</span><span class="w"> </span><span class="nn">st</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Streamlit version:"</span><span class="p">,</span> <span class="n">st</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Streamlit version: 1.51.0
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=ce517031-08ae-4d87-9fd6-89ccaeaae2e8">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span> 
</pre></div>
</div>
</div>
</div>
</div>
</div>
</main>
</body>
</html>
