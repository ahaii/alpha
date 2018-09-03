/**
 * Created by ahaii on 18/8/20.
 */

/**
 * used for server_list del host
 */

function checkboxclick(checkbox){
    if (checkbox.checked){
        $('input:checkbox').prop("checked", true);
    }else {
        $('input:checkbox').prop("checked", false);
    }
}

function delhost() {
    var hostId_arry = [];
    $('input[name="handleHost"]:checkbox').each(function(){
        if ($(this).is(":checked") == true) {
            hostId_arry.push($(this).val());
        }
    });
    if (confirm('是否要删除该主机,然后跑路?') == true) {
        $.ajax({
            type: 'POST',
            url: '/assets/del/',
            dataType: 'json',
            // 注意JSON.stringify()方法,将javascript对象转换为字符串,便于后端接收处理.
            data: {hostid:JSON.stringify(hostId_arry)},
            // traditional默认为false，开启后可以禁止jquery深度序列化参数对象(后端获取参数是，多加了'[]')
            traditional: true,
            success:function(data){
                if (data['result'] == 'ok') {
                    location.reload(true);
                    alert('主机删除成功!');
                }else{
                    alert('主机删除失败!');
                }
            }
        });
    }else{
        return false;
    }
}

/**
 *  used for server_detail save host

function savehost(){
    $.ajax({
        type: 'POST',
        url : '/assets/add/',
        dataType: 'json',
        // serialize()将获取的form数据序列化成'a=1&b=2&c=3&d=4&e=5'格式
        data: $('#server_detail').serialize()
    });
}
 */


/**
 *  used for server_detail expirdate

$(".serverExpirDate").datetimepicker({
    format: 'yyyy-mm-dd',
    language: 'zh-CN',
    weekStart: 1,
    todayBtn: 1,
    autoclose: 1,
    statView: 2,
    todayHighlight: 1,
    minView: 2,
    clearBtn: true,
    forceParse: true
});
*/

/**
 * used for server_detail apps multiple-select

 $('.serverAppMultipleSelect').multipleSelect();
 */

