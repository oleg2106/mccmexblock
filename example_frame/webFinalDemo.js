var state = {'html': '', 'forms': {}},
    mark,
    channel;

var getGrade = function() {
    console.log("call getGrade");
    
    console.log(mark);
    return JSON.stringify(mark);
};

var getState = function() {
    console.log("call getState");
    
    state['#results'] = $("#results").html();
    state['forms']['#form1'] = $('#form1').values();
    
    return JSON.stringify(state);
};

var setState = function (a, params) {
    console.log("call setState");
    console.log(params.data);
    
    if (params.data.state){      
        state = JSON.parse(params.data.state);
        $("#results").html(state['#results']).show();
        for (form_id in state['forms']){
             $(form_id).values(state['forms'][form_id]);
        }
    }
    
    if (params.data.answer){
        mark = JSON.parse(params.data.answer);
    }
};

if (window.parent !== window) {
    channel = Channel.build({
        window: window.parent,
        origin: "*",
        scope: "JSInput"
    });
    channel.bind("getGrade", getGrade);
    channel.bind("getState", getState);
    channel.bind("setState", setState);
}