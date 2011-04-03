// ----------------------------------------------------------------------------
// markItUp!
// ----------------------------------------------------------------------------
summarizationSettings = {
    nameSpace:       "html", // Useful to prevent multi-instances CSS conflict
    onShiftEnter:    {keepDefault:false, replaceWith:'<br />\n'},
    onCtrlEnter:     {keepDefault:false, openWith:'\n<p>', closeWith:'</p>\n'},
    onTab:           {keepDefault:false, openWith:'     '},
    markupSet:  [
        {name:'Text', key:'1', openWith:'<TX(!( class="[![Class]!]")!)>', closeWith:'</TX>', placeHolder:'Tag for text feature' },
        {name:'Number', key:'2', openWith:'<NM(!( class="[![Class]!]")!)>', closeWith:'</NM>', placeHolder:'number represented as quantity (year is not a number)' },
        {name:'Yes/No', key:'3', openWith:'<YN(!( class="[![Class]!]")!)>', closeWith:'</YN>', placeHolder:'Yes/No Value' },
        {name:'Color', key:'4', openWith:'<CL(!( class="[![Class]!]")!)>', closeWith:'</CL>', placeHolder:'Color' },
        {name:'Date', key:'5', openWith:'<DT(!( class="[![Class]!]")!)>', closeWith:'</DT>', placeHolder:'Date' },
        {name:'Model', key:'6', openWith:'<MD(!( class="[![Class]!]")!)>', closeWith:'</MD>', placeHolder:'Model' },
        {separator:'---------------' },
    ]
}
