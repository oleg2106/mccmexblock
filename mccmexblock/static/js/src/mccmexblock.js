/* Javascript for MccmeXBlock. */
function MccmeXBlock(runtime, element, data) {

    var handlerUrl_answer = runtime.handlerUrl(element, 'save_answer');
    var handlerUrl_state  = runtime.handlerUrl(element, 'save_state');
     
    var channel;
     
    $(function ($) {
        /* Here's where you'd do things on page load. */
        var iframe = $('section').find('iframe[name^="iframe_"]').get(0),
            cWindow = iframe.contentWindow,
            path = iframe.src.substring(0, iframe.src.lastIndexOf("/")+1);
        
        channel = Channel.build({
            window: cWindow,
            origin: path,
            scope: "JSInput"
        });
        channel.bind("i_am_ready", function(context, params) {
            console.log(params);
            if ('state' in params && params.state){
                channel.call({
                    method: "getState",
                    success: function(s) {
                        $.ajax({
                            type: "POST",
                            url: handlerUrl_state,
                            data: JSON.stringify({"value": s}),
                        });
                    }
                });
            }

            if ('answer' in params && params.answer){
                channel.call({
                    method: "getGrade",
                    success: function(s) {
                        $.ajax({
                            type: "POST",
                            url: handlerUrl_answer,
                            data: JSON.stringify({"value": s}),
                        });
                    }
                });
            }
        });
        
        channel.call({
            method: "setState",
            params: {data},
            success: function(){}
        });
    });
}
