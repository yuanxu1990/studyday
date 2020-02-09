

//定义函数
// function foo(a,b) {
//     console.log(a);
//     console.log(a+b);
//     return a+b+b
//
// }
//调用函数
// 调用的时候，传入参数可以和定义的参数数量不一致可以不报错
// var re=foo(10)   返回结果 10+undefined+undefined----->NaN
// var re=foo(10,22)
// console.log(re)
//
// //匿名函数
// var func=function (a,b) {
//     console.log("a--->",a);
//     console.log("b---->",b);
//     return a*b;

//}
// console.log("匿名函数--->",func(10,10));

//  立即执行函数
// var ab=(function (a,b) {
//     console.log(a-b);
//     return a+b;
// })(4,3);
// console.log(ab)

// 外部访问不到函数内部的变量，用立即执行函数防止变量污染全局
// 1 函数的调用欧冠，要往回赵 函数的定义阶段
// 2 首先在函数内部找--》内部找不到往外找，直到找到全局为止

// arguments 代表函数内所有的参数
// function f1(a,b) {
//     console.log(a,b);
//     console.log(arguments);
//     var rr=0;
//     for (var i=0;i<arguments.length;i++){
//         rr+=arguments[i]
//         console.log('rr',rr)
//     }
//
// }
// f1(11,22)

// 作用域
// var city="shanghai";
// function Bar() {
//     console.log(city);
//
// }
// function f() {
//     var city="beijig";
//     return Bar;
//
// }
//
// var reta=f()
// reta()


//闭包函数
// var city="Beijing";
// function f(){
//     var city="Shanghai";
//     function inner(){
//         console.log(city);
//     }
//     return inner
// }
// var r=f()
// r()

// js中的词法分析
//  返回结果 undefined 22
/*
js在调用函数的那一瞬间，会先进行词法分析
词法分析过程：
当函数调用的前一瞬间，会先形成一个激活对象：active object（ao），并会分析以下3个方面：
1 函数参数，如果有，则将此参数赋值给ao，且值为undefined。如果没有，则不做任何操作
2 函数局部变量，如果ao上有同名的值，则不做任何操作，如果没有，则将此变量赋值给ao
并且值为undefined
3 函数声明：如果ao上有，则会将ao上的对象覆盖，如果没有，则不做任何操作
 */
// var age=18;
// function foo1() {
//     console.log(age);
//     var age=22;
//     console.log(age);
//
// }
// foo1()


// 执行结果
// ƒ age() {
//         console.log('sdfsdf');
//
//     }
// 22
// 22
// var age=18;
// function foo2(){
//     console.log(age);
//     var age=22;
//     console.log(age);
//     function age() {
//         console.log('sdfsdf');
//
//     }
//     console.log(age);
// }
// foo2()



//JS 内置对象和方法

//1 自定义对象（字典）
// js 对象中，键默认不用加引号，并且自动把单引号转成双引号
//  查找
// var person={"name":"dsfsd","age":38};
// console.log(person);
// console.log(person.name);
// console.log(person.age);
//
// for (var i in person){
//     console.log(i);
//     console.log(person[i]);
// }
//
// // 新增  new 关键字形式
// var per=new Object();
// per.name="dddddd";
// per.age="dsf";
// console.log('per.....',per);


//2 内置的Date对象
//  1 date对象
// var datatime=new Date()
// console.log(datatime)
// console.log(typeof datatime)
// // 字符串时间
// console.log(datatime.toLocaleString())
// console.log(typeof datatime.toLocaleString())


// 成成指定时间的date对象
// var d2=new Date("2020/2/8 14:46")
// console.log(d2.toLocaleString());//转成字符串格式的本地时间
// console.log(d2.toUTCString());//UTC时间

// var d2=new Date()
// //获取日
// console.log(d2.getDate());
// //获取星期
// console.log(d2.getDay());
// //获取月(0-11)
// console.log(d2.getMonth());
// //获取完整年份
// console.log(d2.getFullYear());
// //获取年
// console.log(d2.getYear());
// //获取小时
// console.log(d2.getHours());
// //获取分钟
// console.log(d2.getMinutes());
// //获取秒
// console.log(d2.getSeconds());
// //获取毫秒
// console.log(d2.getMilliseconds())
// //返回累计毫秒数（从1970/1/1）
// console.log(d2.getTime())


//2 json对象
// var str1='{"name":"at","age":189}';
// var str2={name:"age1","age":5525};
//
// //  字符串转json
// var json_str=JSON.parse(str1);
// console.log(json_str,typeof json_str);
// // json转字符串
// var str_json=JSON.stringify(str2);
// console.log(str_json,typeof str_json);



// 3 Math对象


// 4 RegExp 对象 正则模块
/*
参数1 正则表达式中不能含有空格
参数2 匹配模式：常用g（全局匹配：找到所有匹配） 和i（忽略大小写）
用户名只能是英文字母 数字和_ 并且首字母必须是英文字母，长度最短不能少于6位 最长不能超过12位
var reg1=new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$");
匹配相应的字符传
var s1="aa123";

test方法 测试一个字符串是否符合对应的正则规则，返回true和false
var reg1=new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$");
var reg2=reg1.test('aaaa_2');

另外一种
/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test("aaaa_2");

*/

//js中的正则坑一  正则中不能有空格
// 正则中{5,11}加入了空格  这样即使字符串符合匹配规则也报false
// var reg1=new RegExp("^[a-zA-Z][a-zA-Z0-9]{5, 11}$");
// // var reg2=reg1.test("aaaa_a")
// // console.log(reg2)


//js中的正则坑二 当传入为空时 默认传入undefined
// console.log(/^[a-zA-Z][a-zA-Z0-9_]{5,11}$/.test(undefined));
// console.log(/^[0-9][a-zA-Z0-9_]{5,11}$/.test("undefined"));
// console.log(/^[0-9][a-zA-Z0-9_]{5,11}$/.test());


// js中正则坑三
//  当正则表达式 使用了全局模式g的时候，并且还检测一个字符串
// 此时回引出一个lastindex的概念，lastindex会记住上一次匹配成功的位置
//  这也是为什么 下方打印了四次匹配结果 会出现true false true false的原因

console.log("=======================")
var r=/yuan/g;
console.log(r.test("yuan"));
console.log(r.lastIndex);
console.log(r.test("yuan"));
console.log(r.test("yuan"));
console.log(r.test("yuan"));





// js中正则坑三  如果使用replace替换的化，不改变原字符串，需要生成一个新的字符串
// 可以在替换中直接使用正则替换 g代表全部替换  i代表不区分大小写

// var ss="Alexddaiai";
// var s1=ss.replace(/a/gi,"uu");
// console.log(s1);