function showDeviceList(){
      invokeWebApi('/devices',
                   prepareData({}),
                   function(data){
                      render_devicelist("devicelist", data.results)
                   }
                  )
}
function render_devicelist(div_id, sessions){
    var $cycle_panel = $("#"+div_id).html('');
    var $device_table = $('<table>').attr('class','table table-bordered table-hover');
    var $th =     '<thead><tr>'+
                      '<th width="5%"></th>'+
                      '<th width="15%">Machine</th>'+
                      '<th width="25%">Device#</th>'+
                      '<th width="20%">Product</th>'+
                      '<th width="35%">Build</th>'+
                      '</tr></thead>';
    var $tbody = '<tbody></tbody>';
    $device_table.append($th);
    $device_table.append($tbody);
    $cycle_panel.append($device_table);
    for(var t = 0; t < sessions.length; t++) {
        var value = sessions[t];
        var css = value.deviceid !== '' ? "style='background-color:#4682B4'":"style='background-color:#8C8C8C'";
        $tr = "<tr class='info'>"+
                  "<td "+css+"></td>"+
                  "<td>"+value.ip+"</td>"+
                  "<td>"+value.deviceid+"</td>"+
                  "<td>"+value.product+"</td>"+                                    
                  "<td>"+value.build+"</td>"+
                  "</tr>";
        $device_table.append($tr);
    }
}


var AppRouter = Backbone.Router.extend({
    routes: {
        "":"showDefault"
    },
    showDefault: function(){
        showDeviceList();
    }
});
var index_router = new AppRouter;
Backbone.history.start();
