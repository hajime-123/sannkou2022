
namespace PLCPCconnectionTool
{
    // 定数設定一覧
    public static class GlbSetVal
    {
        // ソフト名
        public const string PROGRAM_NAME = "PLCPCconnectionTool";


        // ログファイルリネーム回数
        public const int RENAME_COUNT = 1000;

        // PLC Dデバイスアドレス
        // PLCより読込むファイル名　7110～7114
        public const string PLC_D_FILENAME = "7110";

        // PLCデータ取得トリガー
        public const string PLC_D_PLC_READY = "7100";

        // PC Ready
        public const string PLC_D_PC_READY = "7000";

        // PLC command
        public const string PLC_D_PLC_COMMAND = "7101";

        // PC Save
        public const string PLC_D_PC_SAVE = "7001";

        // PLC ファイル名用タイムスタンプ
        public const string PLC_D_YMD = "7150";
        public const string PLC_D_HOUR = "7153";

        // PLC ログログファイル内タイムスタンプ 7140-7145
        public const string PLC_D_LOG_TIME = "7140";

        // PLC ログファイル内IDコード 7120-7138
        public const string PLC_D_LOG_ID_CODE = "7120";

        // PLC ログファイル内使用列数
        public const string PLC_D_LOG_COLUMN = "7160";

        // PLC ログファイル内データ 7200-7999
        public const string PLC_D_LOG_DATA = "7200";


        // ルートフォルダ
        public const string Root_DIR = @"C:\" + PROGRAM_NAME;

        // INIファイルパス、ファイル名
        public const string INI_FILE = Root_DIR + @"\param.ini";

        // エラーログファイルパス
        public const string ERR_LOG_DIR = @"C:\" + PROGRAM_NAME + @"\ErrLog";
        public const string ERR_LOG_PATH = ERR_LOG_DIR + @"\ErrLog_";

        public const int ERR_DEL_DAYS = 5;

        //// システムログファイルパス
        //public const string SYSTEM_LOG_DIR = @"C:\" + PROGRAM_NAME + @"\SystemLog";
        //public const string SYSTEM_LOG_PATH = SYSTEM_LOG_DIR + @"\SystemLog_";


        //// IO関連（CONTEC社製）
        //public const string IO_DEVICE_NAME = "DIO000";


        // CONTEC IO Bit No.

        //public const byte IO_PLC_Ready = 0;
        //public const byte IO_PC_Ready = 0;
        //public const byte IO_EMERGENCY = 1;
        //public const byte IO_Inspection_Start = 3;
        //public const byte IO_Inspection_End = 3;
        //public const byte IO_GrabTrigger = 4;
        //public const byte IO_GrabFinished = 4;
        //public const byte IO_Weight_Judge = 5;
        //public const byte IO_WorkUmu = 6;
        //public const byte IO_Judge = 6;

        //public const byte IO_WeightValue_PutOK = 2;
        //public const byte IO_WeightValue_GetOK = 2;

        //public const byte IO_KonaAlert = 15;
        //public const byte IO_Recv_HeadNum1 = 10;
        //public const byte IO_Recv_HeadNum2 = 11;
        //public const byte IO_Recv_HeadNum3 = 12;
        //public const byte IO_Send_HeadNum1 = 10;
        //public const byte IO_Send_HeadNum2 = 11;
        //public const byte IO_Send_HeadNum3 = 12;

        //public const short IO_Detect_LotSum = 13;
        //public const short IO_Done_LotLog = 13;




    }
}
