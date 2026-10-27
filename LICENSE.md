# ライセンスと適用範囲

Copyright (c) 2026 d-muramatsu

本リポジトリのオリジナル部分を、下表の対象ごとに許諾します。同じ内容についてCC BYとMITの好きな方を選ぶ二者択一ではありません。許諾は許諾者が保有し、許諾できる権利の範囲に限ります。

| 対象パス・内容 | 適用ライセンス |
| --- | --- |
| `README.md`、`CONTRIBUTING.md`、`LICENSE.md`、`LICENSE-STATUS.md`のオリジナルな説明文 | CC BY 4.0 |
| `docs/*.md`のオリジナルなガイドライン本文・文例・表・図（`docs/battle.md`のテキスト図を含む）、出典への独自の解説 | CC BY 4.0 |
| `checklists/*.md`、`templates/*.md`のオリジナルなチェックリスト・テンプレート | CC BY 4.0 |
| `scripts/*.py`、`tests/*.py`のPythonソース、コメント、docstring、ソフトウェアテスト | MIT |
| `.gitignore`、`.gitattributes`のソフトウェア関連設定 | MIT |
| `LICENSES/CC-BY-4.0.txt`、`LICENSES/MIT.txt` | ライセンス本文。上記の創作物として再許諾するものではなく、各本文に記載された条件をそのまま収録 |

現行の管理対象ファイルはこの表で網羅しています。新しい種類のファイルを追加する際は適用範囲を明記してください。文書をテストの入力として読むだけで、その文書がMITに変わることはありません。

## 文書: Creative Commons Attribution 4.0 International

対象のオリジナル文書・図・テンプレートは、[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)で提供します。[同梱の正式本文](LICENSES/CC-BY-4.0.txt)が適用されます。共有・翻案時には、適切な表示、元資料とライセンスへのリンク、変更した場合の表示、提供されている著作権・免責表示等の保持が必要です。追加的な法的・技術的制限や、著者による推奨・公認を示唆しないでください。

表示名には公開GitHub名 **d-muramatsu** を使用できます。例えば、文書を抜粋・編集して共有する場合は次のように表示します（実際の変更内容・使用箇所に合わせてください）。

> 「レトロRPG UI/UXガイドライン」© 2026 d-muramatsu より、戦闘ガイドを抜粋・編集。原典: [retro-rpg-uiux-guidelines](https://github.com/d-muramatsu/retro-rpg-uiux-guidelines)。[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。資料は無保証です。[適用範囲](https://github.com/d-muramatsu/retro-rpg-uiux-guidelines/blob/main/LICENSE.md)。変更: 例文を自作ゲーム向けに置換。

変更しない場合は変更したと書かず、翻訳・抜粋等の実態を記します。これは表示例であり、正式本文を置き換える追加条件ではありません。資料は正式本文の定める範囲で無保証です。CC BY 4.0は条件を守る利用者に与えた許諾を、後から任意に取り消すことはできません。

## ソフトウェア: MIT

上表のPythonコード・テスト・設定には[MIT License](LICENSES/MIT.txt)を適用します。コピーまたは実質的な部分に著作権表示と許諾表示を含めてください。無保証等の条件は同梱本文のとおりです。MIT本文中の「associated documentation」は、上表でCC BY 4.0を指定したガイドライン文書をMITに変更するものではありません。

## 第三者資料とゲーム制作への適用

Microsoft Xbox Accessibility Guidelines、W3C等の参照先本文・画像・商標・第三者の素材は、このリポジトリのCC BY 4.0／MITによる許諾対象ではありません。それぞれ元の権利・利用条件が適用されます。この除外説明は、第三者資料をコピーする許可を与えるものではありません。引用等に適用される法令上の例外は別途扱われます。[出典・検証日](docs/sources.md)を確認してください。

ガイドラインの考え方を参考にしてゲームを設計するだけで、そのゲーム全体にCC BY 4.0やMITが自動的に適用されることはありません。文書・図・テンプレートの表現をコピー・翻訳・翻案する場合と、ソフトウェアコードをコピーする場合は、それぞれの対象ライセンスの条件を確認してください。

## 正式本文の出所

確認日: **2026-10-26**。ゲーム設計資料の既存の検証日は変更していません。

- CC BY 4.0: [公式の法的本文](https://creativecommons.org/licenses/by/4.0/legalcode.txt)。同梱テキストは[Creative Commons自身の公開ソース](https://github.com/creativecommons/cc-legal-tools-data/blob/main/docs/licenses/by/4.0/legalcode.txt)から取得し、改変せず収録しています。
- MIT: [Open Source Initiativeの正式本文](https://opensource.org/license/mit)。年と公開表示名のプレースホルダーを補い、許諾・条件・免責の文言は改変していません。
