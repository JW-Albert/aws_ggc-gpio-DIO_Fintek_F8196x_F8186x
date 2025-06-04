# AWS Greengrass GPIO 元件 (Fintek F81866/F81966)

本專案實現了一個用於監控和控制 Fintek F81866/F81966 晶片 GPIO 引腳的 Greengrass 元件。它提供即時 GPIO 狀態監控，並將當前狀態更新到 AWS IoT Device Shadow。

## 功能特點

- 即時 GPIO 狀態監控
- AWS IoT Device Shadow 整合
- 支援 Fintek F81866/F81966 晶片
- 可配置的日誌級別
- 自動狀態同步

## 系統需求

- AWS Greengrass Core v2
- Python 3.10 或更高版本
- Fintek F81866/F81966 晶片
- GPIO 存取需要 root 權限

## 安裝步驟

1. 複製此儲存庫
2. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```

## 配置說明

元件需要以下參數：

- `--thing-name`：AWS IoT Thing 名稱
- `--shadow-name`：AWS IoT Shadow 名稱
- `--log-level`：日誌級別（預設：INFO）

## 使用方式

此元件可作為 Greengrass 元件部署。它將：

1. 初始化 GPIO 引腳
2. 監控 GPIO 狀態變化
3. 使用當前狀態更新 AWS IoT Device Shadow
4. 提供狀態變化的即時日誌記錄

## 開發說明

專案結構：
```
.
├── src/
│   ├── main.py          # 主要元件邏輯
│   ├── justRead.py      # GPIO 讀取工具
│   └── lib/             # Fintek 晶片函式庫
├── recipe.yaml         # Greengrass 元件配方
├── requirements.txt    # Python 依賴套件
└── README.md          # 說明文件
```

## 授權說明

[請在此處添加授權資訊] 