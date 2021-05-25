#string function methods
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"
"""
#escape characters

"""
Code Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""

< body >

< div
id = "tryitLeaderboard" >
< !-- TryitLeaderboard -->

< !-- < pre > try_it_leaderboard, all: [320, 50][728, 90][468, 60] < / pre > -->
< div
id = "snhb-try_it_leaderboard-0"
style = ""
data - google - query - id = "COm_sKbF2PACFc-LZgId5WgOPg" > < div
id = "google_ads_iframe_/22152718/sws-hb//w3schools.com//try_it_leaderboard_0__container__"
style = "border: 0pt none;" > < iframe
id = "google_ads_iframe_/22152718/sws-hb//w3schools.com//try_it_leaderboard_0"
title = "3rd party ad content"
name = "google_ads_iframe_/22152718/sws-hb//w3schools.com//try_it_leaderboard_0"
width = "728"
height = "90"
scrolling = "no"
marginwidth = "0"
marginheight = "0"
frameborder = "0"
allow = "conversion-measurement 'src'"
srcdoc = ""
data - google - container - id = "3"
style = "border: 0px; vertical-align: bottom;"
data - load - complete = "true" > < / iframe > < / div > < / div >
< !-- adspace
tryit -->

< / div >

< div


class ="trytopnav" >

< div


class ="w3-bar" style="overflow:auto" >

< a
id = "tryhome"
href = "https://www.w3schools.com"
target = "_blank"
title = "w3schools.com Home"


class ="w3-button w3-bar-item topnav-icons fa fa-home" style="font-size:28px;margin-top:-2px" > < / a >

< a
href = "javascript:void(0);"
onclick = "openMenu()"
id = "menuButton"
title = "Open Menu"


class ="w3-dropdown-click w3-button w3-bar-item topnav-icons fa fa-menu" style="font-size:28px;margin-top:-2px" > < / a >

< a
href = "javascript:void(0);"
onclick = "restack(currentStack)"
title = "Change Orientation"


class ="w3-button w3-bar-item topnav-icons fa fa-rotate" style="font-size:28px;margin-top:-2px" > < / a >

< button


class ="w3-bar-item w3-button topnav-icons fa fa-adjust" onclick="retheme()" title="Change Theme" style="font-size:28px;margin-top:-2px;width:58px;" > < / button >

< button
style = "font-size:16px"


class ="w3-button w3-bar-item ws-green w3-hover-white" onclick="submitTryit(1);ga('send', 'event', 'runCodePython', 'click');snhb.queue.push(function(){googletag.pubads().setTargeting('page_section',(function () {var folder = location.pathname;folder = folder.replace('/', ''); folder = folder.substr(0, folder.indexOf('/')); return folder + 'tryitUA'; })());snhb.startAuction(['try_it_leaderboard']);});" > Run » < / button >

< span


class ="w3-right w3-hide-medium w3-hide-small" style="padding:8px 8px 8px 8px;display:block" > < / span >

< span


class ="w3-right w3-hide-small" style="padding:8px 0;display:block;float:right;" > < span id="framesize" > Result Size: <


    span > 391
x
476 < / span > < / span > < / span >
< / div >

< / div >
< div
id = "shield"
style = "display: none;" > < / div >
< a
href = "javascript:void(0)"
id = "dragbar"
style = "width: 5px; top: 138px; left: 400.5px; height: 476px; cursor: col-resize;" > < / a >
< div
id = "container" >
< div
id = "navbarDropMenu"


class ="w3-dropdown-content w3-bar-block w3-border" style="z-index:5" >

< span
onclick = "openMenu()"


class ="w3-button w3-display-topright w3-transparent w3-hover-dark-grey" title="Close Menu" style="font-weight:bold;padding-top:10px;padding-bottom:11px;" > × < / span >

< div


class ="w3-bar-block" >

< a


class ="w3-bar-item w3-button" href="javascript:void(0);" title="Change Orientaton" onclick="openMenu();restack(currentStack)" > < i class ="fa fa-rotate" style="font-size:26px;margin-left:-4px;margin-right:8px" > < / i > < span style="position:relative;top:-4px;left:2px;" > Change Orientation < / span > < / a >

< / div >
< footer


class ="w3-container w3-small ws-grey" >

< p > < a
style = "display:inline;padding:0;"
href = "/about/about_privacy.asp"
target = "_blank"
onclick = "openMenu();"


class ="w3-hover-none ws-hover-text-green" > Privacy policy < / a > and

< a
style = "display:inline;padding:0;"
href = "/about/about_copyright.asp"
target = "_blank"
onclick = "openMenu();"


class ="w3-hover-none ws-hover-text-green" > Copyright 1999-2021 < / a > < / p >

< / footer >
< / div >
< div
id = "menuOverlay"


class ="w3-overlay w3-transparent" style="cursor:pointer;z-index:4" > < / div >

< div
id = "textareacontainer" >
< div
id = "textarea" >
< div
id = "textareawrapper" >
< textarea
autocomplete = "off"
id = "textareaCode"
wrap = "logical"
spellcheck = "false"
style = "display: none;" > txt = "We are the so-called \"Vikings\" from the north."
print(txt)
< / textarea > < div


class ="CodeMirror cm-s-default CodeMirror-wrap" > < div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8px; left: 65.7344px;" > < textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0" > < / textarea > < / div > < div class ="CodeMirror-vscrollbar" cm- not -content="true" > < div style="min-width: 1px; height: 0px;" > < / div > < / div > < div class ="CodeMirror-hscrollbar" cm- not -content="true" > < div style="height: 100%; min-height: 1px; width: 0px;" > < / div > < / div > < div class ="CodeMirror-scrollbar-filler" cm- not -content="true" > < / div > < div class ="CodeMirror-gutter-filler" cm- not -content="true" > < / div > < div class ="CodeMirror-scroll" tabindex="-1" > < div class ="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: -17px; border-right-width: 13px; min-height: 80px; padding-right: 0px; padding-bottom: 0px;" > < div style="position: relative; top: 0px;" > < div class ="CodeMirror-lines" > < div style="position: relative; outline: none;" > < div class ="CodeMirror-measure" > < pre > x < / pre > < / div > < div class ="CodeMirror-measure" > < / div > < div style="position: relative; z-index: 1;" > < div class ="CodeMirror-selected" style="position: absolute; left: 61.7344px; top: 0px; width: 317.266px; height: 18px;" > < / div > < div class ="CodeMirror-selected" style="position: absolute; left: 4px; top: 18px; width: 375px; height: 18px;" > < / div > < div class ="CodeMirror-selected" style="position: absolute; left: 4px; top: 36px; width: 90.75px; height: 18px;" > < / div > < / div > < div class ="CodeMirror-cursors" style="" > < / div > < div class ="CodeMirror-code" > < pre class =" CodeMirror-line " > < span style="padding-right: 0.1px;" > < span class ="cm-variable" > txt < / span > < span class ="cm-operator" >= < / span > < span class ="cm-string" > "We are the so-called \"Vikings\" from the north." < / span > < / span > < / pre > < pre class =" CodeMirror-line " > < span style="padding-right: 0.1px;" > < span class ="cm-builtin" > print < / span > ( < span


class ="cm-variable" > txt < / span > ) < / span > < / pre > < pre


class =" CodeMirror-line " > < span style="padding-right: 0.1px;" > < span cm-text="" > ​ < / span > < / span > < / pre > < / div > < / div > < / div > < / div > < / div > < div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 80px;" > < / div > < div class ="CodeMirror-gutters" style="display: none; height: 93px;" > < / div > < / div > < / div >

< form
id = "codeForm"
autocomplete = "off"
style = "margin:0px;display:none;"
action = "https://try.w3schools.com/try_python.php?x=0.22010978118646318"
method = "post"
accept - charset = "utf-8"
target = "iframeResult" >
< input
type = "hidden"
name = "code"
id = "code"
value = "txt w3equalsign &quot;We are the so-called \&quot;Vikings\&quot; from the north.&quot;
print(txt)
">
< / form >
< / div >
< / div >
< / div >
< div
id = "iframecontainer" >
< div
id = "iframe" >
< div
id = "runloadercontainer"
style = "width: 668px; height: 476px; display: none;" > < div
id = "runloader"
style = "width: 133.6px; height: 133.6px; top: 171.203px;" > < / div > < / div >
< div
id = "iframewrapper" > < iframe
frameborder = "0"
id = "iframeResult"
name = "iframeResult" > < / iframe > < / div >
< / div >
< / div >
< / div >
< script >

function
submitTryit(n)
{
if (window.editor)
{
    window.editor.save();
}
var
text = document.getElementById("textareaCode").value;
var
ifr = document.createElement("iframe");
ifr.setAttribute("frameborder", "0");
ifr.setAttribute("id", "iframeResult");
ifr.setAttribute("name", "iframeResult");
document.getElementById("iframewrapper").innerHTML = "";
document.getElementById("iframewrapper").appendChild(ifr);
document.getElementById("iframeResult").addEventListener("load", hideSpinner);
displaySpinner();
var
t = text;
t = t.replace( /= / gi, "w3equalsign");
t = t.replace( /\+ / gi, "w3plussign");
var
pos = t.search( / script / i)
while (pos > 0) {
t=t.substring(0, pos) + "w3" + t.substr(pos, 3) + "w3" + t.substr(pos+3, 3) + "tag" + t.substr(pos+6);
pos=t.search( / script / i);
}
document.getElementById("code").value = t;
document.getElementById("codeForm").action = "https://try.w3schools.com/try_python.php?x=" + Math.random();
document.getElementById('codeForm').method = "post";
document.getElementById('codeForm').acceptCharset = "utf-8";
document.getElementById('codeForm').target = "iframeResult";
document.getElementById("codeForm").submit();
}

function
hideSpinner()
{
document.getElementById("runloadercontainer").style.display = "none";
}
function
displaySpinner()
{
var
i, c, w, h, r, top;
i = document.getElementById("iframeResult");
w = w3_getStyleValue(i, "width");
h = w3_getStyleValue(i, "height");
c = document.getElementById("runloadercontainer");
c.style.width = w;
c.style.height = h;
c.style.display = "block";
w = Number(w.replace("px", "")) / 5;
r = document.getElementById("runloader");
r.style.width = w + "px";
r.style.height = w + "px";
h = w3_getStyleValue(r, "height");
h = Number(h.replace("px", "")) / 2;
top = w3_getStyleValue(c, "height");
top = Number(top.replace("px", "")) / 2;
top = top - h
r.style.top = top + "px";
}


var
currentStack = true;
if ((window.screen.availWidth <= 768 & & window.innerHeight > window.innerWidth) | | "" == " horizontal")
{restack(true);}
function
restack(horizontal)
{
var
tc, ic, t, i, c, f, sv, sh, d, height, flt, width;
tc = document.getElementById("textareacontainer");
ic = document.getElementById("iframecontainer");
t = document.getElementById("textarea");
i = document.getElementById("iframe");
c = document.getElementById("container");
sv = document.getElementById("stackV");
sh = document.getElementById("stackH");
tc.className = tc.className.replace("horizontal", "");
ic.className = ic.className.replace("horizontal", "");
t.className = t.className.replace("horizontal", "");
i.className = i.className.replace("horizontal", "");
c.className = c.className.replace("horizontal", "");
if (sv) {sv.className = sv.className.replace("horizontal", "")};
if (sv) {sh.className = sh.className.replace("horizontal", "")};
stack = "";
if (horizontal) {
tc.className = tc.className + " horizontal";
ic.className = ic.className + " horizontal";
t.className = t.className + " horizontal";
i.className = i.className + " horizontal";
c.className = c.className + " horizontal";
if (sv) {sv.className = sv.className + " horizontal"};
if (sv) {sh.className = sh.className + " horizontal"};
stack = " horizontal";
document.getElementById("textareacontainer").style.height = "50%";
document.getElementById("iframecontainer").style.height = "50%";
document.getElementById("textareacontainer").style.width = "100%";
document.getElementById("iframecontainer").style.width = "100%";
currentStack=false;
} else {
document.getElementById("textareacontainer").style.height = "100%";
document.getElementById("iframecontainer").style.height = "100%";
document.getElementById("textareacontainer").style.width = "50%";
document.getElementById("iframecontainer").style.width = "50%";
currentStack=true;
}
fixDragBtn();
showFrameSize();
}
function
retheme()
{
var
cc = document.body.className;
if (cc.indexOf("darktheme") > -1) {
document.body.className = cc.replace("darktheme", "");
if (opener) {opener.document.body.className = cc.replace("darktheme", "");}
localStorage.setItem("preferredmode", "light");
} else {
document.body.className += " darktheme";
if (opener) {opener.document.body.className += " darktheme";}
localStorage.setItem("preferredmode", "dark");
}
}
(
function
setThemeMode()
{
    var
x = localStorage.getItem("preferredmode");
if (x == "dark")
{
    document.body.className += " darktheme";
}
})();
function
showFrameSize()
{
var
t;
var
width, height;
width = Number(w3_getStyleValue(document.getElementById("iframeResult"), "width").replace("px", "")).toFixed();
height = Number(w3_getStyleValue(document.getElementById("iframeResult"), "height").replace("px", "")).toFixed();
document.getElementById("framesize").innerHTML = "Result Size: <span>" + width + " x " + height + "</span>";
}
var
dragging = false;
var
stack;
function
fixDragBtn()
{
var
textareawidth, leftpadding, dragleft, containertop, buttonwidth
var
containertop = Number(w3_getStyleValue(document.getElementById("container"), "top").replace("px", ""));
if (stack != " horizontal") {
document.getElementById("dragbar").style.width = "5px";
textareasize = Number(w3_getStyleValue(document.getElementById("textareawrapper"), "width").replace("px", ""));
leftpadding = Number(w3_getStyleValue(document.getElementById("textarea"), "padding-left").replace("px", ""));
buttonwidth = Number(w3_getStyleValue(document.getElementById("dragbar"), "width").replace("px", ""));
textareaheight = w3_getStyleValue(document.getElementById("textareawrapper"), "height");
dragleft = textareasize + leftpadding + (leftpadding / 2) - (buttonwidth / 2);
document.getElementById("dragbar").style.top = containertop + "px";
document.getElementById("dragbar").style.left = dragleft + "px";
document.getElementById("dragbar").style.height = textareaheight;
document.getElementById("dragbar").style.cursor = "col-resize";

} else {
document.getElementById("dragbar").style.height = "5px";
if (window.getComputedStyle) {
textareawidth = window.getComputedStyle(document.getElementById("textareawrapper"), null).getPropertyValue("height");
textareaheight = window.getComputedStyle(document.getElementById("textareawrapper"), null).getPropertyValue("width");
leftpadding = window.getComputedStyle(document.getElementById("textarea"), null).getPropertyValue("padding-top");
buttonwidth = window.getComputedStyle(document.getElementById("dragbar"), null).getPropertyValue("height");
} else {
dragleft = document.getElementById("textareawrapper").currentStyle["width"];
}
textareawidth = Number(textareawidth.replace("px", ""));
leftpadding = Number(leftpadding.replace("px", ""));
buttonwidth = Number(buttonwidth.replace("px", ""));
dragleft = containertop + textareawidth + leftpadding + (leftpadding / 2);
document.getElementById("dragbar").style.top = dragleft + "px";
document.getElementById("dragbar").style.left = "5px";
document.getElementById("dragbar").style.width = textareaheight;
document.getElementById("dragbar").style.cursor = "row-resize";
}
}
function
dragstart(e)
{
e.preventDefault();
dragging = true;
var
main = document.getElementById("iframecontainer");
}
function
dragmove(e)
{
if (dragging)
    {
        document.getElementById("shield").style.display = "block";
    if (stack != " horizontal") {
    var percentage = (e.pageX / window.innerWidth) * 100;
    if (percentage > 5 & & percentage < 98) {
    var mainPercentage = 100-percentage;
    document.getElementById("textareacontainer").style.width = percentage + "%";
    document.getElementById("iframecontainer").style.width = mainPercentage + "%";
    fixDragBtn();
    }
    } else {
    var containertop = Number(w3_getStyleValue(document.getElementById("container"), "top").replace("px", ""));
    var percentage = ((e.pageY - containertop + 20) / (window.innerHeight - containertop + 20)) * 100;
    if (percentage > 5 & & percentage < 98) {
    var mainPercentage = 100-percentage;
    document.getElementById("textareacontainer").style.height = percentage + "%";
    document.getElementById("iframecontainer").style.height = mainPercentage + "%";
    fixDragBtn();
    }
    }
    showFrameSize();
    }
}
function
dragend()
{
document.getElementById("shield").style.display = "none";
dragging = false;
var
vend = navigator.vendor;
if (window.editor & & vend.indexOf("Apple") == -1) {
window.editor.refresh();
}
}
if (window.addEventListener) {
document.getElementById("dragbar").addEventListener("mousedown", function(e)
{dragstart(e);});
document.getElementById("dragbar").addEventListener("touchstart", function(e)
{dragstart(e);});
window.addEventListener("mousemove", function(e)
{dragmove(e);});
window.addEventListener("touchmove", function(e)
{dragmove(e);});
window.addEventListener("mouseup", dragend);
window.addEventListener("touchend", dragend);
window.addEventListener("load", fixDragBtn);
window.addEventListener("load", showFrameSize);
}


function
colorcoding()
{
var
ua = navigator.userAgent;
// Opera
Mini
refreshes
the
page
when
trying
to
edit
the
textarea.
if (ua & & ua.toUpperCase().indexOf("OPERA MINI") > -1) {
return false;}
window.editor = CodeMirror.fromTextArea(document.getElementById("textareaCode"), {
    mode: "text/x-python",
    lineWrapping: true,
    smartIndent: false
});
// window.editor.on("change", function()
{window.editor.save();});
}
colorcoding();

function
w3_getStyleValue(elmnt, style)
{
if (window.getComputedStyle)
{
return window.getComputedStyle(elmnt, null).getPropertyValue(style);
} else {
return elmnt.currentStyle[style];
}
}

function
openMenu()
{
    var
x = document.getElementById("navbarDropMenu");
var
y = document.getElementById("menuOverlay");
var
z = document.getElementById("menuButton");
if (z.className.indexOf("w3-text-gray") == -1)
{
z.className += " w3-text-gray";
} else {
z.className = z.className.replace(" w3-text-gray", "");
}
if (z.className.indexOf("w3-gray") == -1) {
z.className += " w3-gray";
} else {
z.className = z.className.replace(" w3-gray", "");
}
if (x.className.indexOf("w3-show") == -1) {
x.className += " w3-show";
} else {
x.className = x.className.replace(" w3-show", "");
}
if (y.className.indexOf("w3-show") == -1) {
y.className += " w3-show";
} else {
y.className = y.className.replace(" w3-show", "");
}

}
// When
the
user
clicks
anywhere
outside
of
the
modal, close
it
window.onclick = function(event)
{
if (event.target == document.getElementById("menuOverlay"))
{
openMenu();
}
}
< / script >

    < iframe
name = "__tcfapiLocator"
style = "display: none;" > < / iframe > < iframe
name = "__uspapiLocator"
style = "display: none;" > < / iframe > < iframe
id = "google_osd_static_frame_622111159598"
name = "google_osd_static_frame"
style = "display: none; width: 0px; height: 0px;" > < / iframe > < / body ><body>

<div id="tryitLeaderboard">
<!-- TryitLeaderboard -->

  <!--<pre>try_it_leaderboard, all: [320,50][728,90][468,60]</pre>-->
  <div id="snhb-try_it_leaderboard-0" style="" data-google-query-id="COm_sKbF2PACFc-LZgId5WgOPg"><div id="google_ads_iframe_/22152718/sws-hb//w3schools.com//try_it_leaderboard_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/22152718/sws-hb//w3schools.com//try_it_leaderboard_0" title="3rd party ad content" name="google_ads_iframe_/22152718/sws-hb//w3schools.com//try_it_leaderboard_0" width="728" height="90" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" allow="conversion-measurement 'src'" srcdoc="" data-google-container-id="3" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div>
  <!-- adspace tryit-->

</div>

<div class="trytopnav">
<div class="w3-bar" style="overflow:auto">
  <a id="tryhome" href="https://www.w3schools.com" target="_blank" title="w3schools.com Home" class="w3-button w3-bar-item topnav-icons fa fa-home" style="font-size:28px;margin-top:-2px"></a>
  <a href="javascript:void(0);" onclick="openMenu()" id="menuButton" title="Open Menu" class="w3-dropdown-click w3-button w3-bar-item topnav-icons fa fa-menu" style="font-size:28px;margin-top:-2px"></a>
  <a href="javascript:void(0);" onclick="restack(currentStack)" title="Change Orientation" class="w3-button w3-bar-item topnav-icons fa fa-rotate" style="font-size:28px;margin-top:-2px"></a>
  <button class="w3-bar-item w3-button topnav-icons fa fa-adjust" onclick="retheme()" title="Change Theme" style="font-size:28px;margin-top:-2px;width:58px;"></button>
  <button style="font-size:16px" class="w3-button w3-bar-item ws-green w3-hover-white" onclick="submitTryit(1);ga('send', 'event', 'runCodePython', 'click');snhb.queue.push(function(){googletag.pubads().setTargeting('page_section',(function () {var folder = location.pathname;folder = folder.replace('/', ''); folder = folder.substr(0, folder.indexOf('/')); return folder + 'tryitUA'; })());snhb.startAuction(['try_it_leaderboard']);});">Run »</button>
  <span class="w3-right w3-hide-medium w3-hide-small" style="padding:8px 8px 8px 8px;display:block"></span>
  <span class="w3-right w3-hide-small" style="padding:8px 0;display:block;float:right;"><span id="framesize">Result Size: <span>391 x 476</span></span></span>
</div>

</div>
<div id="shield" style="display: none;"></div>
<a href="javascript:void(0)" id="dragbar" style="width: 5px; top: 138px; left: 400.5px; height: 476px; cursor: col-resize;"></a>
<div id="container">
<div id="navbarDropMenu" class="w3-dropdown-content w3-bar-block w3-border" style="z-index:5">
<span onclick="openMenu()" class="w3-button w3-display-topright w3-transparent w3-hover-dark-grey" title="Close Menu" style="font-weight:bold;padding-top:10px;padding-bottom:11px;">×</span>
  <div class="w3-bar-block">
    <a class="w3-bar-item w3-button" href="javascript:void(0);" title="Change Orientaton" onclick="openMenu();restack(currentStack)"><i class="fa fa-rotate" style="font-size:26px;margin-left:-4px;margin-right:8px"></i><span style="position:relative;top:-4px;left:2px;">Change Orientation</span></a>
  </div>
  <footer class="w3-container w3-small ws-grey">
  <p><a style="display:inline;padding:0;" href="/about/about_privacy.asp" target="_blank" onclick="openMenu();" class="w3-hover-none ws-hover-text-green">Privacy policy</a> and
  <a style="display:inline;padding:0;" href="/about/about_copyright.asp" target="_blank" onclick="openMenu();" class="w3-hover-none ws-hover-text-green">Copyright 1999-2021</a></p>
  </footer>
</div>
<div id="menuOverlay" class="w3-overlay w3-transparent" style="cursor:pointer;z-index:4"></div>
  <div id="textareacontainer">
    <div id="textarea">
      <div id="textareawrapper">
        <textarea autocomplete="off" id="textareaCode" wrap="logical" spellcheck="false" style="display: none;">txt = "We are the so-called \"Vikings\" from the north."
print(txt)
</textarea><div class="CodeMirror cm-s-default CodeMirror-wrap"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 8px; left: 65.7344px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: -17px; border-right-width: 13px; min-height: 80px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre>x</pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"><div class="CodeMirror-selected" style="position: absolute; left: 61.7344px; top: 0px; width: 317.266px; height: 18px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 18px; width: 375px; height: 18px;"></div><div class="CodeMirror-selected" style="position: absolute; left: 4px; top: 36px; width: 90.75px; height: 18px;"></div></div><div class="CodeMirror-cursors" style=""></div><div class="CodeMirror-code"><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-variable">txt</span> <span class="cm-operator">=</span> <span class="cm-string">"We are the so-called \"Vikings\" from the north."</span></span></pre><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-variable">txt</span>) </span></pre><pre class=" CodeMirror-line "><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 80px;"></div><div class="CodeMirror-gutters" style="display: none; height: 93px;"></div></div></div>
        <form id="codeForm" autocomplete="off" style="margin:0px;display:none;" action="https://try.w3schools.com/try_python.php?x=0.22010978118646318" method="post" accept-charset="utf-8" target="iframeResult">
          <input type="hidden" name="code" id="code" value="txt w3equalsign &quot;We are the so-called \&quot;Vikings\&quot; from the north.&quot;
print(txt)
">
        </form>
       </div>
    </div>
  </div>
  <div id="iframecontainer">
    <div id="iframe">
      <div id="runloadercontainer" style="width: 668px; height: 476px; display: none;"><div id="runloader" style="width: 133.6px; height: 133.6px; top: 171.203px;"></div></div>
      <div id="iframewrapper"><iframe frameborder="0" id="iframeResult" name="iframeResult"></iframe></div>
    </div>
  </div>
</div>
<script>

function submitTryit(n) {
  if (window.editor) {
    window.editor.save();
  }
  var text = document.getElementById("textareaCode").value;
  var ifr = document.createElement("iframe");
  ifr.setAttribute("frameborder", "0");
  ifr.setAttribute("id", "iframeResult");
  ifr.setAttribute("name", "iframeResult");
  document.getElementById("iframewrapper").innerHTML = "";
  document.getElementById("iframewrapper").appendChild(ifr);
  document.getElementById("iframeResult").addEventListener("load", hideSpinner);
  displaySpinner();
  var t=text;
  t=t.replace(/=/gi,"w3equalsign");
  t=t.replace(/\+/gi,"w3plussign");
  var pos=t.search(/script/i)
  while (pos>0) {
    t=t.substring(0,pos) + "w3" + t.substr(pos,3) + "w3" + t.substr(pos+3,3) + "tag" + t.substr(pos+6);
    pos=t.search(/script/i);
  }
  document.getElementById("code").value=t;
  document.getElementById("codeForm").action = "https://try.w3schools.com/try_python.php?x=" + Math.random();
  document.getElementById('codeForm').method = "post";
  document.getElementById('codeForm').acceptCharset = "utf-8";
  document.getElementById('codeForm').target = "iframeResult";
  document.getElementById("codeForm").submit();
}

function hideSpinner() {
  document.getElementById("runloadercontainer").style.display = "none";
}
function displaySpinner() {
  var i, c, w, h, r, top;
  i = document.getElementById("iframeResult");
  w = w3_getStyleValue(i, "width");
  h = w3_getStyleValue(i, "height");
  c = document.getElementById("runloadercontainer");
  c.style.width = w;
  c.style.height = h;
  c.style.display = "block";
  w = Number(w.replace("px", "")) / 5;
  r = document.getElementById("runloader");
  r.style.width = w + "px";
  r.style.height = w + "px";
  h = w3_getStyleValue(r, "height");
  h = Number(h.replace("px", "")) / 2;
  top = w3_getStyleValue(c, "height");
  top = Number(top.replace("px", "")) / 2;
  top = top - h
  r.style.top = top + "px";
}


var currentStack=true;
if ((window.screen.availWidth <= 768 && window.innerHeight > window.innerWidth) || "" == " horizontal") {restack(true);}
function restack(horizontal) {
    var tc, ic, t, i, c, f, sv, sh, d, height, flt, width;
    tc = document.getElementById("textareacontainer");
    ic = document.getElementById("iframecontainer");
    t = document.getElementById("textarea");
    i = document.getElementById("iframe");
    c = document.getElementById("container");
    sv = document.getElementById("stackV");
    sh = document.getElementById("stackH");
    tc.className = tc.className.replace("horizontal", "");
    ic.className = ic.className.replace("horizontal", "");
    t.className = t.className.replace("horizontal", "");
    i.className = i.className.replace("horizontal", "");
    c.className = c.className.replace("horizontal", "");
    if (sv) {sv.className = sv.className.replace("horizontal", "")};
    if (sv) {sh.className = sh.className.replace("horizontal", "")};
    stack = "";
    if (horizontal) {
        tc.className = tc.className + " horizontal";
        ic.className = ic.className + " horizontal";
        t.className = t.className + " horizontal";
        i.className = i.className + " horizontal";
        c.className = c.className + " horizontal";
        if (sv) {sv.className = sv.className + " horizontal"};
        if (sv) {sh.className = sh.className + " horizontal"};
        stack = " horizontal";
        document.getElementById("textareacontainer").style.height = "50%";
        document.getElementById("iframecontainer").style.height = "50%";
        document.getElementById("textareacontainer").style.width = "100%";
        document.getElementById("iframecontainer").style.width = "100%";
        currentStack=false;
    } else {
        document.getElementById("textareacontainer").style.height = "100%";
        document.getElementById("iframecontainer").style.height = "100%";
        document.getElementById("textareacontainer").style.width = "50%";
        document.getElementById("iframecontainer").style.width = "50%";
        currentStack=true;
    }
    fixDragBtn();
    showFrameSize();
}
function retheme() {
  var cc = document.body.className;
  if (cc.indexOf("darktheme") > -1) {
    document.body.className = cc.replace("darktheme", "");
    if (opener) {opener.document.body.className = cc.replace("darktheme", "");}
    localStorage.setItem("preferredmode", "light");
  } else {
    document.body.className += " darktheme";
    if (opener) {opener.document.body.className += " darktheme";}
    localStorage.setItem("preferredmode", "dark");
  }
}
(
function setThemeMode() {
  var x = localStorage.getItem("preferredmode");
  if (x == "dark") {
    document.body.className += " darktheme";
  }
})();
function showFrameSize() {
  var t;
  var width, height;
  width = Number(w3_getStyleValue(document.getElementById("iframeResult"), "width").replace("px", "")).toFixed();
  height = Number(w3_getStyleValue(document.getElementById("iframeResult"), "height").replace("px", "")).toFixed();
  document.getElementById("framesize").innerHTML = "Result Size: <span>" + width + " x " + height + "</span>";
}
var dragging = false;
var stack;
function fixDragBtn() {
  var textareawidth, leftpadding, dragleft, containertop, buttonwidth
  var containertop = Number(w3_getStyleValue(document.getElementById("container"), "top").replace("px", ""));
  if (stack != " horizontal") {
    document.getElementById("dragbar").style.width = "5px";
    textareasize = Number(w3_getStyleValue(document.getElementById("textareawrapper"), "width").replace("px", ""));
    leftpadding = Number(w3_getStyleValue(document.getElementById("textarea"), "padding-left").replace("px", ""));
    buttonwidth = Number(w3_getStyleValue(document.getElementById("dragbar"), "width").replace("px", ""));
    textareaheight = w3_getStyleValue(document.getElementById("textareawrapper"), "height");
    dragleft = textareasize + leftpadding + (leftpadding / 2) - (buttonwidth / 2);
    document.getElementById("dragbar").style.top = containertop + "px";
    document.getElementById("dragbar").style.left = dragleft + "px";
    document.getElementById("dragbar").style.height = textareaheight;
    document.getElementById("dragbar").style.cursor = "col-resize";

  } else {
    document.getElementById("dragbar").style.height = "5px";
    if (window.getComputedStyle) {
        textareawidth = window.getComputedStyle(document.getElementById("textareawrapper"),null).getPropertyValue("height");
        textareaheight = window.getComputedStyle(document.getElementById("textareawrapper"),null).getPropertyValue("width");
        leftpadding = window.getComputedStyle(document.getElementById("textarea"),null).getPropertyValue("padding-top");
        buttonwidth = window.getComputedStyle(document.getElementById("dragbar"),null).getPropertyValue("height");
    } else {
        dragleft = document.getElementById("textareawrapper").currentStyle["width"];
    }
    textareawidth = Number(textareawidth.replace("px", ""));
    leftpadding = Number(leftpadding .replace("px", ""));
    buttonwidth = Number(buttonwidth .replace("px", ""));
    dragleft = containertop + textareawidth + leftpadding + (leftpadding / 2);
    document.getElementById("dragbar").style.top = dragleft + "px";
    document.getElementById("dragbar").style.left = "5px";
    document.getElementById("dragbar").style.width = textareaheight;
    document.getElementById("dragbar").style.cursor = "row-resize";
  }
}
function dragstart(e) {
  e.preventDefault();
  dragging = true;
  var main = document.getElementById("iframecontainer");
}
function dragmove(e) {
  if (dragging)
  {
    document.getElementById("shield").style.display = "block";
    if (stack != " horizontal") {
      var percentage = (e.pageX / window.innerWidth) * 100;
      if (percentage > 5 && percentage < 98) {
        var mainPercentage = 100-percentage;
        document.getElementById("textareacontainer").style.width = percentage + "%";
        document.getElementById("iframecontainer").style.width = mainPercentage + "%";
        fixDragBtn();
      }
    } else {
      var containertop = Number(w3_getStyleValue(document.getElementById("container"), "top").replace("px", ""));
      var percentage = ((e.pageY - containertop + 20) / (window.innerHeight - containertop + 20)) * 100;
      if (percentage > 5 && percentage < 98) {
        var mainPercentage = 100-percentage;
        document.getElementById("textareacontainer").style.height = percentage + "%";
        document.getElementById("iframecontainer").style.height = mainPercentage + "%";
        fixDragBtn();
      }
    }
    showFrameSize();
  }
}
function dragend() {
  document.getElementById("shield").style.display = "none";
  dragging = false;
  var vend = navigator.vendor;
  if (window.editor && vend.indexOf("Apple") == -1) {
      window.editor.refresh();
  }
}
if (window.addEventListener) {
  document.getElementById("dragbar").addEventListener("mousedown", function(e) {dragstart(e);});
  document.getElementById("dragbar").addEventListener("touchstart", function(e) {dragstart(e);});
  window.addEventListener("mousemove", function(e) {dragmove(e);});
  window.addEventListener("touchmove", function(e) {dragmove(e);});
  window.addEventListener("mouseup", dragend);
  window.addEventListener("touchend", dragend);
  window.addEventListener("load", fixDragBtn);
  window.addEventListener("load", showFrameSize);
}


function colorcoding() {
  var ua = navigator.userAgent;
  //Opera Mini refreshes the page when trying to edit the textarea.
  if (ua && ua.toUpperCase().indexOf("OPERA MINI") > -1) { return false; }
  window.editor = CodeMirror.fromTextArea(document.getElementById("textareaCode"), {
    mode: "text/x-python",
    lineWrapping: true,
    smartIndent: false
  });
//  window.editor.on("change", function () {window.editor.save();});
}
colorcoding();

function w3_getStyleValue(elmnt,style) {
    if (window.getComputedStyle) {
        return window.getComputedStyle(elmnt,null).getPropertyValue(style);
    } else {
        return elmnt.currentStyle[style];
    }
}

function openMenu() {
    var x = document.getElementById("navbarDropMenu");
    var y = document.getElementById("menuOverlay");
    var z = document.getElementById("menuButton");
    if (z.className.indexOf("w3-text-gray") == -1) {
        z.className += " w3-text-gray";
    } else {
        z.className = z.className.replace(" w3-text-gray", "");
    }
    if (z.className.indexOf("w3-gray") == -1) {
        z.className += " w3-gray";
    } else {
        z.className = z.className.replace(" w3-gray", "");
    }
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
    if (y.className.indexOf("w3-show") == -1) {
        y.className += " w3-show";
    } else {
        y.className = y.className.replace(" w3-show", "");
    }

}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == document.getElementById("menuOverlay")) {
        openMenu();
    }
}
</script>


<iframe name="__tcfapiLocator" style="display: none;"></iframe><iframe name="__uspapiLocator" style="display: none;"></iframe><iframe id="google_osd_static_frame_622111159598" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;"></iframe></body>