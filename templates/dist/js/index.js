/**
 *
 * Created by Administrator on 2015/12/7.
 */
$(document).ready(function(){
    var item = $(".item");
    var width = item.width();
    if(width>763){
        item.css("height",width/4);
    }
    else {
        item.css("height",width/2);
        item.find('img').css("height",width/2);
    }
});
