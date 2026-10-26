# 実装・レビューリスト

[README](../README.md) / [プレイテスト記録](../templates/playtest.md)

各項目に担当、ビルド、結果（PASS / FAIL / 未実施 / 適用外）、証拠、対応先を記録してください。チェックは実施済みかつ基準を満たした場合だけ付けます。適用外には理由と代替策を記録します。

## P0 — 対象機能の公開前に解消

- [ ] NAV-02: [全画面で決定・戻る・フォーカス](../docs/navigation.md)が一貫し、連打やモーダル背面入力で誤確定しない。
- [ ] BAT-01: [戦闘の対象・消費](../docs/battle.md)が確定前に分かり、取り消しで資源が減らない。
- [ ] BAT-04: [重要な状態変化](../docs/battle.md)を無音・演出短縮でも追える。
- [ ] INV-03: [希少品・一括売却](../docs/inventory-progression.md)の対象・数量・不可逆性を確定前に確認できる。
- [ ] SAV-01: [保存成功と失敗](../docs/save-state.md)が区別され、失敗時に既存データを保護できる。
- [ ] SAV-03: [不可逆な選択](../docs/save-state.md)で失う範囲と保存への影響を説明できる。
- [ ] SAV-04: [敗北・ロード・遷移](../docs/save-state.md)後の状態が説明と一致し、二重入力がない。
- [ ] ACC-01: [必須文字](../docs/accessibility-input.md)が対象表示環境で読め、拡大しても欠けない。
- [ ] ACC-02: [色・音以外の手がかり](../docs/accessibility-input.md)が重要情報にあり、背景との識別を確認した。

## P1 — 通常採用。不採用には理由と検証

- [ ] NAV-01: [判断に必要な情報](../docs/navigation.md)を画面往復なしで比較できる。
- [ ] NAV-03: [一覧位置と無効理由](../docs/navigation.md)を空一覧・末尾削除でも把握できる。
- [ ] EXP-01: [調べられる対象](../docs/exploration-dialogue.md)を総当たり以外の手がかりで発見できる。
- [ ] EXP-02: [目的の再確認](../docs/exploration-dialogue.md)と任意のヒントで再開でき、答えを押し付けない。
- [ ] TXT-01: [文字速度・会話ログ](../docs/exploration-dialogue.md)を利用でき、連打で分岐を誤選択しない。
- [ ] TXT-02: [独自メカニクスの導入](../docs/exploration-dialogue.md)を飛ばしても後で見返せる。
- [ ] BAT-02: [予測と確定結果](../docs/battle.md)、耐性・無効・回避を区別できる。
- [ ] BAT-03: [順序と時間進行](../docs/battle.md)を説明でき、加速・割り込みで矛盾しない。
- [ ] INV-01: [持ち物の用途・数量](../docs/inventory-progression.md)から探し、使用後も位置を保てる。
- [ ] INV-02: [装備の損益](../docs/inventory-progression.md)を特殊効果の喪失も含め比較できる。
- [ ] PRG-01: [成長の効果・条件・振り直し](../docs/inventory-progression.md)を選ぶ前に理解できる。
- [ ] SAV-02: [手動／自動保存](../docs/save-state.md)と復帰地点を識別でき、進行喪失の範囲を把握できる。
- [ ] ACC-03: [演出軽減](../docs/accessibility-input.md)後も選択状態と結果を認識できる。
- [ ] INP-01: [各対応機器](../docs/accessibility-input.md)単独で完結し、割当変更後の案内が正しい。
- [ ] SET-01: [設定の到達・復元・保持](../docs/accessibility-input.md)を新規起動と再開で確認した。

## P2 — 採用した場合に比較検証

- [ ] NAV-04: [短縮操作](../docs/navigation.md)が反復を減らし、誤選択を増やさない。
- [ ] EXT-01: [アクション・ATB](../docs/extensions.md)の時間進行と支援範囲を明示した。
- [ ] EXT-02: [モバイル](../docs/extensions.md)の割り込み・指の遮蔽・再起動を実機で検証した。

## 文書自体の公開レビュー

- [ ] ルールの理由・推奨・例・例外・確認方法があり、優先度が本文と一致する。
- [ ] 出典の本文・適用条件・検証日を確認した。独自提案を外部の義務と呼んでいない。
- [ ] 非公開情報、実参加者の情報、秘密情報、商用ゲームの画像やコピー文を含まない。
- [ ] ローカルリンクと文書チェックを実行し、限界を記録した。
- [ ] ゲームの実機テストは文書検査と区別して報告した。
