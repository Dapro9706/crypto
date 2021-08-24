$('#Encode').click((event)=>{$.get("/back/crypto",{'input':$('#input').val(),'key':$('#key').val(),'reverse':0},function(data){$('#output').val(data.output)})})
$('#Decode').click((event)=>{$.get("/back/crypto",{'input':$('#input').val(),'key':$('#key').val(),'reverse':1},function(data){$('#output').val(data.output)})})
$('#Copy').on("click",function(){document.getElementById('output').select();document.execCommand('copy')})
