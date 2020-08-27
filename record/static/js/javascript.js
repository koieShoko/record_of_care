function functionName()
    {
        var select1 = document.forms.formName.selectName1; //変数select1を宣言
        var select2 = document.forms.formName.selectName2; //変数select2を宣言
        var select3 = document.forms.formName.selectName3; //変数select3を宣言

        
        select2.options.length = 0; // 選択肢の数がそれぞれに異なる場合、これが重要
        select3.options.length = 0; // 選択肢の数がそれぞれに異なる場合、これが重要
           
        var words = {果物:["りんご","みかん","オレンジ"], 野菜:["にんじん","キャベツ","きゅうり"]};
        
        if (select1.options[select1.selectedIndex].value == "果物")
            {
                select2.options[0] = new Option("りんご");
                select2.options[1] = new Option("みかん");
                select2.options[2] = new Option("オレンジ");
            }
         
        else if (select1.options[select1.selectedIndex].value == "野菜")
            {
                select2.options[0] = new Option("キャベツ");
                select2.options[1] = new Option("きゅうり");
                select2.options[2] = new Option("にんんじん");
                select2.options[3] = new Option("たまねぎ");
            }
         
        else if (select1.options[select1.selectedIndex].value == "肉類")
            {
                select2.options[0] = new Option("豚肉");
                select2.options[1] = new Option("牛肉");
            }
    }
 