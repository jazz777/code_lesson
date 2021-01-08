import threading
import zipfile

class AsyncZip(threading.Thread):

    def __init__(self,infile,outfile):
        threading.Thread.__init__(self)
        self.infile=infile
        self.outfile=outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()

        print(self.infile,'のZIPが完了しました')


background=AsyncZip('mydata.txt','mydata.zip')

background.start()
print('メインプログラムはまだ動き続けています')
'''

background.join()
print('メインプログラムはバックグラウンドの処理の終了を待っていました')
'''