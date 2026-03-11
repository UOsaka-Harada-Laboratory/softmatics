# プロジェクト概要
softmatics
NITTA SOFTmatics グリッパーをROS Noetic（Ubuntu 20.04）環境から制御するための非公式パッケージ。シミュレーションおよびArduinoを介した実機制御をサポートします。


## 1. ディレクトリ構造とコンポーネント
本プロジェクトは、主に以下のROSパッケージで構成されます。
- `softmatics_description`: グリッパーのURDF/Xacroモデル定義およびRViz表示用パッケージ。
- `softmatics_gazebo`: Gazeboシミュレーション環境および `ros-control` を用いたジョイント制御用パッケージ。コントローラ設定（`config/control_params.yaml`）を含む。
- `softmatics_device`: Arduinoを介した実機の把持/解放（Grasp/release）トリガー用パッケージ。Arduinoボードに書き込むスケッチ（`sketch/sketch.ino`）を含む。

## 2. 開発と運用の厳格なルール
### A. ビルドと依存関係の制約
- 環境はUbuntu 20.04 PCおよびROS Noetic (Python3) を前提とします。
- ビルド時は必ず `catkin build -DPYTHON_EXECUTABLE=/usr/bin/python3` を使用してPython 3実行環境を指定すること。
- `roboticsgroup_upatras_gazebo_plugins` や `ros-noetic-ros-control`, `ros-noetic-ros-controllers` などの外部依存パッケージが必須です。

### B. シミュレーターと実機の操作
- **シミュレーション**: Gazebo上で `/softmatics/joint_position_controller/command` トピック（`std_msgs/Float64`）に対して目標角度をPublishすることで動作確認を行います。
- **実機制御**: Arduinoにスケッチを書き込んだ後、`softmatics_device` を起動し、`/softmatics_device/toggle` サービスをCallすることでGrasp/Releaseの状態をトグル（ON/OFF）します。

## 3. エージェントのルーティングルール（PMへの指示）
タスクのフェーズに応じて、以下の専門エージェントに的確に委譲してください。
- **アーキテクチャ設計・URDFモデリング設計**: `architect` に依頼
- **ROSパッケージ実装・Arduinoスケッチ記述・Launchファイル作成**: `developer` に依頼
- **ビルド確認・Gazebo/RViz表示・サービステスト**: `tester` に依頼
- **TFエラー・Gazeboコントローラ起動失敗・Arduino通信エラーの解消**: `debugger` に依頼