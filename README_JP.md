<br>

<p align="center">
    <img alt="GPUStack" src="https://raw.githubusercontent.com/gpustack/gpustack/main/docs/assets/gpustack-logo.png" width="300px"/>
</p>
<br>

<p align="center">
    <a href="https://docs.gpustack.ai" target="_blank">
        <img alt="Documentation" src="https://img.shields.io/badge/ドキュメント-GPUStack-blue?logo=readthedocs&logoColor=white"></a>
    <a href="./LICENSE" target="_blank">
        <img alt="License" src="https://img.shields.io/github/license/gpustack/gpustack?logo=github&logoColor=white&label=License&color=blue"></a>
    <a href="./docs/assets/wechat-group-qrcode.jpg" target="_blank">
        <img alt="WeChat" src="https://img.shields.io/badge/微信群-GPUStack-blue?logo=wechat&logoColor=white"></a>
    <a href="https://discord.gg/VXYJzuaqwD" target="_blank">
        <img alt="Discord" src="https://img.shields.io/badge/Discord-GPUStack-blue?logo=discord&logoColor=white"></a>
    <a href="https://twitter.com/intent/follow?screen_name=gpustack_ai" target="_blank">
        <img alt="Follow on X(Twitter)" src="https://img.shields.io/twitter/follow/gpustack_ai?logo=X"></a>
</p>
<br>

<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README_CN.md">简体中文</a> |
  <a href="./README_JP.md">日本語</a>
</p>

<br>

## 概要

GPUStack は、効率的な AI モデルデプロイメントのために設計されたオープンソースの GPU クラスタマネージャーです。独自の GPU ハードウェア上でモデルを効率的に実行できるように、最適な推論エンジンの選択、GPU リソースのスケジューリング、モデルアーキテクチャの分析、デプロイメントパラメータの自動設定を行います。

以下の図は、GPUStack が最適化されていない vLLM ベースラインと比較して、どのように推論スループットを向上させるかを示しています：

![a100-throughput-comparison](docs/assets/a100-throughput-comparison.png)

詳細なベンチマーク方法と結果については、[推論パフォーマンスラボ](https://docs.gpustack.ai/latest/performance-lab/overview/)をご覧ください。

## テスト済み推論エンジン、GPU、およびモデル

GPUStack はプラグインアーキテクチャを採用しており、新しい AI モデル、推論エンジン、GPU ハードウェアの追加が容易です。パートナーやオープンソースコミュニティと緊密に連携し、様々な推論エンジンと GPU 間で新興モデルのテストと最適化を行っています。以下は、現在サポートされている推論エンジン、GPU、モデルのリストです。これらは時間の経過とともに拡大を続けます。

**テスト済み推論エンジン:**

- vLLM
- SGLang
- TensorRT-LLM
- MindIE

**テスト済み GPU:**

- NVIDIA A100
- NVIDIA H100/H200
- Ascend 910B

**チューニング済みモデル:**

- Qwen3
- gpt-oss
- GLM-4.5-Air
- GLM-4.5/4.6
- DeepSeek-R1

## アーキテクチャ

GPUStack は、開発チーム、IT 組織、およびサービスプロバイダーが大規模なモデルサービスを提供できるようにします。LLM、音声、画像、ビデオモデル向けの業界標準 API をサポートしています。このプラットフォームには、組み込みのユーザー認証とアクセス制御、GPU パフォーマンスと使用率のリアルタイム監視、トークン使用量と API リクエストレートの詳細なメータリングが含まれています。

以下の図は、単一の GPUStack サーバーがオンプレミスとクラウド環境の両方にまたがる複数の GPU クラスタをどのように管理できるかを示しています。GPUStack スケジューラは、リソース使用率を最大化するために GPU を割り当て、最適なパフォーマンスを得るために適切な推論エンジンを選択します。管理者は、統合された Grafana および Prometheus ダッシュボードを通じて、システムの健全性とメトリクスに関する完全な可視性も得ます。

![gpustack-v2-architecture](docs/assets/gpustack-v2-architecture.png)

GPUStack は、AI モデルをデプロイするための強力なフレームワークを提供します。その中核的な機能は以下の通りです：

- **マルチクラスタ GPU 管理:** 複数の環境にわたる GPU クラスタを管理します。これには、オンプレミスサーバー、Kubernetes クラスタ、およびクラウドプロバイダが含まれます。
- **プラグ可能な推論エンジン:** vLLM、SGLang、TensorRT-LLM などの高性能推論エンジンを自動的に設定します。必要に応じてカスタム推論エンジンを追加することもできます。
- **パフォーマンス最適化設定:** 低レイテンシまたは高スループット向けの事前調整済みモードを提供します。GPUStack は、LMCache や HiCache などの拡張 KV キャッシュシステムをサポートし、TTFT を削減します。また、EAGLE3、MTP、N-gram などの投機的デコード手法の組み込みサポートも含まれます。
- **エンタープライズグレードの運用:** 自動化された障害回復、負荷分散、監視、認証、およびアクセス制御のサポートを提供します。

## クイックスタート

### 前提条件

1.  少なくとも 1 つの NVIDIA GPU を搭載したノード。他の GPU タイプについては、GPUStack UI で worker を追加する際のガイドラインを参照するか、詳細については[インストールドキュメント](https://docs.gpustack.ai/latest/installation/requirements/)を参照してください。
2.  worker ノードに NVIDIA ドライバー、[Docker](https://docs.docker.com/engine/install/)、[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) がインストールされていることを確認してください。
3.  （オプション）GPUStack server をホストするための CPU ノード。GPUStack server は GPU を必要とせず、CPU のみのマシンで実行できます。[Docker](https://docs.docker.com/engine/install/) がインストールされている必要があります。Docker Desktop（Windows および macOS 用）もサポートされています。専用の CPU ノードがない場合は、GPU worker ノードと同じマシンに GPUStack server をインストールできます。
4.  GPUStack worker ノードは Linux のみをサポートしています。Windows を使用する場合は、WSL2 の使用を検討し、Docker Desktop の使用は避けてください。macOS は GPUStack worker ノードとしてサポートされていません。

### GPUStack のインストール

以下のコマンドを実行して、Docker を使用して GPUStack server をインストールし起動します：

```bash
sudo docker run -d --name gpustack \
    --restart unless-stopped \
    -p 80:80 \
    -p 10161:10161 \
    --volume gpustack-data:/var/lib/gpustack \
    gpustack/gpustack
```

<details>
<summary>代替案：Quay コンテナレジストリミラーの使用</summary>

`Docker Hub` からイメージをプルできない場合やダウンロードが非常に遅い場合は、`quay.io` を指定することで当社のミラーを使用できます：

```bash
sudo docker run -d --name gpustack \
    --restart unless-stopped \
    -p 80:80 \
    -p 10161:10161 \
    --volume gpustack-data:/var/lib/gpustack \
    quay.io/gpustack/gpustack \
    --system-default-container-registry quay.io
```

</details>

GPUStack の起動ログを確認します：

```bash
sudo docker logs -f gpustack
```

GPUStack が起動したら、以下のコマンドを実行してデフォルトの管理者パスワードを取得します：

```bash
sudo docker exec gpustack cat /var/lib/gpustack/initial_admin_password
```

ブラウザを開き、`http://あなたのホストIP` にアクセスして GPUStack UI にアクセスします。デフォルトのユーザー名 `admin` と上記で取得したパスワードを使用してログインします。

### GPU クラスターのセットアップ

1.  GPUStack UI で、`Clusters` ページに移動します。
2.  `Add Cluster` ボタンをクリックします。
3.  クラスタープロバイダーとして `Docker` を選択します。
4.  新しいクラスターの `Name` と `Description` フィールドに入力し、`Save` ボタンをクリックします。
5.  UI のガイドラインに従って新しい worker ノードを設定します。worker ノードを GPUStack server に接続するには、worker ノードで Docker コマンドを実行する必要があります。コマンドは以下のようになります：
    ```bash
    sudo docker run -d --name gpustack-worker \
          --restart=unless-stopped \
          --privileged \
          --network=host \
          --volume /var/run/docker.sock:/var/run/docker.sock \
          --volume gpustack-data:/var/lib/gpustack \
          --runtime nvidia \
          gpustack/gpustack \
          --server-url http://your_gpustack_server_url \
          --token your_worker_token \
          --advertise-address 192.168.1.2
    ```
6.  worker ノードでこのコマンドを実行して GPUStack server に接続します。
7.  worker ノードが正常に接続されると、GPUStack UI の `Workers` ページに表示されます。

### モデルのデプロイ

1. GPUStack UI の`Catalog`ページに移動します。

2. 利用可能なモデルのリストから`Qwen3 0.6B`モデルを選択します。

3. デプロイ互換性チェックが通過した後、`Save`ボタンをクリックしてモデルをデプロイします。

![カタログからqwen3をデプロイ](docs/assets/quick-start/quick-start-qwen3.png)

4. GPUStack はモデルファイルのダウンロードとモデルのデプロイを開始します。デプロイステータスが`Running`と表示されたら、モデルは正常にデプロイされています。

![モデルが実行中](docs/assets/quick-start/model-running.png)

5. ナビゲーションメニューで`Playground - Chat`をクリックし、右上の`Model`ドロップダウンからモデル`qwen3-0.6b`が選択されていることを確認します。これで UI プレイグラウンドでモデルとチャットできるようになります。

![クイックチャット](docs/assets/quick-start/quick-chat.png)

### API 経由でモデルを使用

1. ユーザーアバターにカーソルを合わせて`API Keys`ページに移動し、`New API Key`ボタンをクリックします。

2. `Name`を入力し、`Save`ボタンをクリックします。

3. 生成された API キーをコピーし、安全な場所に保存します。このキーは作成時に一度しか確認できないことに注意してください。

4. これで、この API キーを使用して、GPUStack が提供する OpenAI 互換の API エンドポイントにアクセスできます。例えば、以下のように curl を使用します：

```bash
# `your_api_key` と `your_gpustack_server_url` を
# 実際のAPIキーとGPUStackサーバーのURLに置き換えてください。
export GPUSTACK_API_KEY=your_api_key
curl http://your_gpustack_server_url/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $GPUSTACK_API_KEY" \
  -d '{
    "model": "qwen3-0.6b",
    "messages": [
      {
        "role": "system",
        "content": "あなたは役立つアシスタントです。"
      },
      {
        "role": "user",
        "content": "ジョークを教えてください。"
      }
    ],
    "stream": true
  }'
```

## ドキュメント

完全なドキュメントについては、[公式ドキュメントサイト](https://docs.gpustack.ai)を参照してください。

## ビルド

1. Python（バージョン 3.10 から 3.12）をインストールします。

2. `make build`を実行します。

ビルドされた wheel パッケージは`dist`ディレクトリにあります。

## 貢献

GPUStack への貢献に興味がある場合は、[貢献ガイド](./docs/contributing.md)をお読みください。

## コミュニティに参加

問題がある場合、または提案がある場合は、お気軽に私たちの[コミュニティ](https://discord.gg/VXYJzuaqwD)に参加してサポートを受けてください。

## ライセンス

Copyright (c) 2024-2025 The GPUStack authors

Apache License, Version 2.0（「ライセンス」）に基づいてライセンスされます。
ライセンスに準拠しない限り、このファイルを使用することはできません。
ライセンスのコピーは[LICENSE](./LICENSE)ファイルで入手できます。

適用される法律で要求されない限り、または書面で合意されない限り、本ライセンスに基づいて配布されるソフトウェアは、明示黙示を問わず、いかなる保証も条件もなしに「現状のまま」配布されます。
ライセンスの権利と制限を規定する特定の言語については、ライセンスを参照してください。
