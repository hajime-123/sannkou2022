using System;
using System.Text;

namespace PLCPCconnectionTool
{
    public static class ErrorCheck
    {

        public static void subErrCk(Exception ex, String strLocation, String strFileDetail) // エラーログの出力
        {
            // Lock用オブジェクト
            object objLock = new object();

            // エラーログの書込み
            lock (objLock)
            {
               

                // エラーログファイル名の作成
                String strFileName = GlbSetVal.ERR_LOG_PATH + strFileDetail + ".log";
                
                using (System.IO.StreamWriter Writer = new System.IO.StreamWriter(strFileName, true, Encoding.Default))
                {

                    Writer.Write(DateTime.Now);             // エラー発生日時
                    Writer.Write("\t" + strLocation);      // エラー発生場所
                    Writer.WriteLine("\t" + ex.Message);   // エラー内容

                }
            }
        }

    }
}
