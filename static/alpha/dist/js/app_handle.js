/**
 * Created by ahaii on 18/9/3.
 */

function checkboxclick(checkbox){
    if (checkbox.checked){
        $('input:checkbox').prop("checked", true);
    }else {
        $('input:checkbox').prop("checked", false);
    }
}

function delapp() {
    var appId_arry = [];
    $('input[name="handleApp"]:checkbox').each(function(){
        if ($(this).is(":checked") == true) {
            appId_arry.push($(this).val());
        }
    });
    if (appId_arry ===  undefined || appId_arry.length == 0){
        alert('未选择任何应用!');
        return false;
    }
    if (confirm('是否要删除该应用,然后跑路?') == true) {
        $.ajax({
            type: 'POST',
            url: '/app/del/',
            dataType: 'json',
            // 注意JSON.stringify()方法,将javascript对象转换为字符串,便于后端接收处理.
            data: {appid:JSON.stringify(appId_arry)},
            // traditional默认为false，开启后可以禁止jquery深度序列化参数对象(后端获取参数是，多加了'[]')
            traditional: true,
            success:function(data){
                if (data['result'] == 'ok') {
                    location.reload(true);
                    alert('应用删除成功!');
                }else{
                    alert('应用删除失败!');
                }
            }
        });
    }else{
        return false;
    }
}