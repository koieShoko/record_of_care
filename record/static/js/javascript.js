




function set_option(select, candidates){
    for (let i = 0; i < candidates.length; i++){
        select.options[i] = new Option(candidates[i]);
    }
    alert("aa");
    return;
}
/*
$("#form0").on('change', function()
{    
    alert("a");
    var form0_candidates = ["食事","入浴", "生活","医療","夜間", "リハビリ", "家族連絡", "事故", "その他"];        
    var form1_candidates = {
        食事     : ["朝食", "昼食", "夕食"], 
        入浴     : ["有り", "無し"],
        夜間     : ["",""],
        生活     : ["", ""],
        医療     : ["", ""],
        リハビリ : ["", ""],
        家族連絡 : ["", ""],
        事故     : ["", ""],
        その他   : ["", ""]
    };
    var select0 = document.forms.formName.form0; //変数select0を宣言
    var select1 = document.forms.formName.form1; //変数select1を宣言
    select1.options.length = 0; // 選択肢の数がそれぞれに異なる場合、これが重要
    form0_candidates.forEach(function(form0_candidate){
    alert("b");
    if (select0.options[select0.selectedIndex].value == form0_candidate)
    {
        set_option(select1, form1_candidates[form0_candidate]);
        break;
    }else{
        continue;
    }
        return;
    });
});
*/

