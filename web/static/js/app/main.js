function showDeviceList(){
      invokeWebApi('/devices',
                   prepareData({}),
                   function(data){
                      render_devicelist("devicelist", data.results)
                   }
                  )
}
function render_devicelist(div_id, records){
    var $cycle_panel = $("#"+div_id).html('');
    var $device_table = $('<table>').attr('class','table table-bordered table-hover');
    var $th =     '<thead><tr>'+
                      '<th width="5%"></th>'+
                      '<th width="15%">PI</th>'+
                      '<th width="10%">TAG</th>'+
                      '<th width="10%">DUT#</th>'+
                      '<th width="10%">Platform</th>'+
                      '<th width="10%">Product</th>'+
                      '<th width="25%">Build</th>'+
                      '</tr></thead>';
    var $tbody = '<tbody></tbody>';
    var $tr = "";
    $device_table.append($th);
    $device_table.append($tbody);
    $cycle_panel.append($device_table);
    for(var t = 0; t < records.length; t++) {
        var record = records[t];
        var ip = record.ip;
        var mac = record.mac;
        var api = record.api;
        var id = "";
        var Platform = "";
        var Product = "";
        var Build = "";
        var devices;
        var status;
        var css = 'style="background-color:grey"';
        if(api !== undefined) {
            devices = api.devices;
            status = api.status;
            for (Platform in devices) {
              var dd_list = devices[Platform];
              if(status == "up")
                  css = 'style="background-color:green"';
              else
                  css = 'style="background-color:yellow"';

              for(var k = 0; k < dd_list.length; k++) {
                  var dd = dd_list[k];
                  id = dd.adb.serial;
                  Product = dd.product.model;
                  Build = dd.build.display_id;
                  $tr = "<tr class='info'>"+
                            "<td "+css+"></td>"+
                            "<td>"+ip+"</td>"+
                            "<td>"+mac+"</td>"+
                            "<td>"+id+"</td>"+
                            "<td>"+Platform+"</td>"+
                            "<td>"+Product+"</td>"+
                            "<td>"+Build+"</td>"+
                            "</tr>"; 
                  $device_table.append($tr);
              }
           }
        } else {
                $tr = "<tr class='info'>"+
                          "<td "+css+"></td>"+
                          "<td>"+ip+"</td>"+
                          "<td>"+mac+"</td>"+
                          "<td>"+id+"</td>"+
                          "<td>"+Platform+"</td>"+
                          "<td>"+Product+"</td>"+
                          "<td>"+Build+"</td>"+
                          "</tr>";
                $device_table.append($tr);
        }
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
