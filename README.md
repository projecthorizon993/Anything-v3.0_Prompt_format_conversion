# stable-diffusion-Prompt-format-quick-conversion
There are many prompt formats for stable diffusion, including () and {}, etc. I personally like to use (1girl: 2.0), which solves the problem of messy text
stable diffusion的Prompt format 非常多,有()以及{}等,我個人喜歡使用(1girl: 2.0),他解決了文字雜亂的問題<br>
# Use 使用
He is just a simple Python program.<br>
All you need to do is install python and you can run.<br>
Download my .py file and use cmd to enter it under the path:python spell_text.py<br>

他只是一個簡單的Python程式<br>
你只需要安裝 python 便可以運行<br>
下載我的.py檔案 用cmd 在路徑下輸入:python spell_text.py<br>
# Function 功能
       Enter the prompt and weight Format:prompt,weight example:1girl,2.0
       Enter -i or info get more information
       You can enter continuously or with a single input
       Enter 0 to leave the loop and display the result.
       
       The program will automatically delete the input {}() and newline
       following is an example
       {masterpiece},2.0 -->(masterpiece:2.0)
       masterpiece,1.5,best quality,1.3,Highest image quality,1.2 -->(masterpiece:1.5),(best quality:1.3),(Highest image quality:1.2),
       
       
       輸入Prompt及權重 格式為:標籤,權重 如:1girl,2.0
       輸入 -i or info 獲取更多資訊
       您可以連續輸入或單次輸入
       輸入 0 退出迴圈並顯示結果。
# future plans 未來計畫
我想做一個自動排序標籤的排序方法，<br>
但是Python的操作畫面不太理想，以後會用C#開發。<br>
# Example diagram

