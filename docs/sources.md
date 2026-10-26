# 出典・適用範囲

[README](../README.md)

以下はすべて Microsoft Learn の一次資料です。**検証日: 2026-10-26**。各リンクを開き、題名・本文・関連する原則を確認しました。元ページのゲーム画像・文章を転載していません。本資料の日本語文例・図・RPGへの具体化は編集上の提案であり、実験で効果を立証したという主張ではありません。

| 資料 | 参考にした範囲 | 本資料での対応 | 適用上の注意 |
| --- | --- | --- | --- |
| [XAG 101: Text display](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101) | 読める文字と表示設定 | ACC-01 | 元のサイズ推奨は出力・視距離の条件付き。内部低解像度へ直結させない |
| [XAG 102: Contrast](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102) | 前景と背景の識別 | ACC-02 | 数値は文字サイズ・対象・出力条件に依存。UI全体を一律の比率で判定しない |
| [XAG 103: Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/103) | 複数の知覚手段 | EXP-01、BAT-04、ACC-02 | 色以外の記号だけで非視覚利用全体を満たすわけではない |
| [XAG 107: Input](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/107) | 入力の選択、代替 | INP-01、EXT-01、EXT-02 | 対応機器・プラットフォームを定義して検証する |
| [XAG 108: Game difficulty options](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/108) | 難易度の選択と進行喪失を減らす保存 | SAV-02、SET-01 | 作品の難度設計と操作上の障壁を区別する |
| [XAG 109: Objective clarity](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/109) | 目的、振り返り、セーブの識別情報 | EXP-02、TXT-02、PRG-01、SAV-02 | 段階ヒントや戦闘予測は本資料による応用 |
| [XAG 112: UI navigation](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112) | 一貫性、フォーカス、設定への到達 | NAV-01〜04、INV-01、SET-01 | 1次元リストの循環を格子の全端へ機械的に適用しない |
| [XAG 115: Error messages and destructive actions](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/115) | エラーの説明、不可逆操作の保護 | INV-03、SAV-01、SAV-03 | ロック、買い戻し、安全な初期選択は具体化の提案 |
| [XAG 116: Time limits](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/116) | 読解・操作の時間、手動の会話送り | TXT-01、EXT-01 | 中核ゲームメカニクスと非中核UIの時間制約を区別する |
| [XAG 117: Visual distractions and motion settings](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117) | 動くUIと画面揺れ等の設定 | ACC-03、EXT-01 | CRT風効果の切替はレトロ表現への応用。安全性認証ではない |

## 外部基準との境界

本資料は XAG の全文・認証チェックリストではありません。正式に XAG を評価する場合は、対象ガイドライン本文の条件・例外・適用範囲を直接確認してください。W3C WCAGやCOGAの考え方を参照する場合も、Web向けの条件を低解像度ゲームへ無条件に移植したり、ゲーム全体のWCAG適合を宣言したりしません。今回は直接検証したゲーム向け一次資料を中核に採用しました。

コスト・対象予告、装備差分、確定前キャンセル無消費、保存状態表、プレイテスト課題は本ガイドの設計判断です。出典がそれらの唯一の正解を定めているとは扱いません。

## 更新の手順

リンクの疎通だけで検証済みにせず、本文と対象条件を読み直します。更新時は日付と影響したルールIDを記録し、数値や適合表現を追加する場合は元の適用条件も記載します。比較研究やユーザー調査の結果を記す場合は、実施条件・参加者範囲・限界を添えてください。
