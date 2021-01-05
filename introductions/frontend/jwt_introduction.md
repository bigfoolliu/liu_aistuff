# JWT

<!-- vim-markdown-toc Marked -->

* [1.基本知识](#1.基本知识)
    - [1.1介绍](#1.1介绍)
    - [1.2组成](#1.2组成)
        + [1.2.1头部(header)](#1.2.1头部(header))
        + [1.2.2载荷(payload)](#1.2.2载荷(payload))
        + [1.2.3签名(signature)](#1.2.3签名(signature))
* [2.使用](#2.使用)
    - [2.1授权(Authorization)](#2.1授权(authorization))
    - [2.2信息交换(Information Exchange,)](#2.2信息交换(information-exchange,))
    - [3.token](#3.token)

<!-- vim-markdown-toc -->

## 1.基本知识

### 1.1介绍

- [基本介绍](https://pyjwt.readthedocs.io/en/latest/)
- [更多使用](https://pyjwt.readthedocs.io/en/latest/usage.html)
- [jwt使用详解](https://learnku.com/articles/17883?order_by=vote_count&)

- `JSON Web Token`，通常简称为JWT，它是一种开放标准（RFC 7519）
- 随着RESTful架构的流行，越来越多的项目使用JWT`作为用户身份认证的方式`
- JWT相当于是三个JSON对象经过编码后，用.分隔并组合到一起，这三个JSON对象分别是头部（header）、载荷（payload）和签名(signature), 因此典型的JWT格式为：`xxx.xxx.xxx`

### 1.2组成

#### 1.2.1头部(header)

```json
{
  "alg": "HS256",  alg属性表示签名的算法，默认是HMAC SHA256（简写成HS256）
  "typ": "JWT"     typ属性表示这个令牌的类型，JWT中都统一书写为JWT
}
```

#### 1.2.2载荷(payload)

- 载荷部分用来`存放实际需要传递的数据`
- 包含声明（要求）, 声明是关于实体(通常是用户)和其他数据的声明
- 声明有三种类型
    - `registered`, 预定义的，不是强制的，但是推荐
    - `public`，可以随意定义的
    - `private`，用于在同意使用它们的各方之间共享信息，并且不是注册的或公开的声明

```sh
iss  # 签发人, jwt签发者, str     
jti  # 编号, jwt的唯一身份标识，主要用来作为一次性token, str
sub  # 主题, jwt所面向的用户, str
aud  # 受众, 接收jwt的一方, str
exp  # 过期时间, jwt的过期时间，这个过期时间必须要大于签发时间, int
nbf  # 生效时间, 定义在什么时间之前，该jwt都是不可用的, int
iat  # 签发时间, int
```

#### 1.2.3签名(signature)

- `签名部分是对前面两部分生成一个指纹，防止数据伪造和篡改`
- 实现签名首先需要指定一个`密钥`，这个密钥只有服务器才知道，不能泄露给用户
- 然后，使用头部指定的签名算法（默认是HS256），按照下面的公式产生签名: `HS256(base64Encode(header) + '.' + base64Encode(payload), secret)`，最外围是用密钥为secret的HS256，所以核心是要保护密钥
- 算出签名以后，把`头部、载荷、签名三个部分拼接成一个字符串`，每个部分用.进行分隔，这样一个JWT就生成好了

## 2.使用

### 2.1授权(Authorization)

- JWT的最常见场景, `一旦用户登录，后续每个请求都将包含JWT`，允许用户访问该令牌允许的路由、服务和资源
- token请求时候放置位置：
  - 放在header中，推荐，且需要`将服务器设置为接受来自所有域的请求`，用`Access-Control-Allow-Origin: *`
  - 放在url的参数中，`?token=123`
- token放置在客户端的三种方式
  - LocalStorage
  - SessionStorage
  - Cookie(`不能设置HTTP-Only，但因此需要防范xss攻击`), 推荐，前两个存在跨域读取限制
- 无状态，无会话，可扩展，更加安全，因为不使用cookie(直接放在请求头)，可以防止CSRF攻击
- token能够撤回，可以使特定的一组token失效
- 优于移动端不支持cookie，可以使用token鉴权
- 与OAuth的区别：OAuth是一种授权框架，JWT是一种授权认证协议
- 续签问题，一段实际爱你没请求的时候，：
  - web端，一般设置为1-2小时
  - 移动端， 一般谁在为15-30 天

具体步骤：

1. 用户携带用户名和密码请求访问
2. 服务器校验用户凭据
3. 应用提供一个token给客户端
4. 客户端存储token，并且在随后的每一次请求中都带着它
5. 服务器校验token并返回数据

```sh
# HMAC 算法是不可逆算法，类似 MD5 和 hash ，但多一个密钥，密钥（即上面的 secret）由服务端持有，客户端把 token 发给服务端后，服务端可以把其中的头部和载荷再加上事先共享的 secret 再进行一次 HMAC 加密，得到的结果和 token 的第三段进行对比，如果一样则表明数据没有被篡改。
```

### 2.2信息交换(Information Exchange,)

对于安全的在各方之间传输信息而言，JSON Web Tokens无疑是一种很好的方式。因为JWT可以被签名，例如，用公钥/私钥对，你可以确定发送人就是它们所说的那个人。另外，由于签名是使用头和有效负载计算的，您还可以验证内容没有被篡改。

### 3.token

- [深入理解token](https://www.cnblogs.com/xuxinstyle/p/9675541.html)
- [python产生token以及token的验证方法](https://www.jb51.net/article/153525.htm)
- [阮一峰:json web token入门教程](http://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html)

- `令牌`，服务端生成的一串字符串，作为客户端请求的标识
- token可以发在cookie里面，但是这样不能解决跨域问题
- token做好发在请求头`Authorization`里面

**优缺点**：

- 完全由应用管理，可以避开`同源策略`(同源指`两个页面的协议，端口和域名都相同`，同源策略指不同源的客户端脚本在没有明确授权的情况下不可以读写对方的资源)
- 可以是`无状态`的，可以在多个服务器之间共享
- 可以`减轻服务器压力`，减少频繁查询数据库
- 更容易实现水平扩展，因为令牌保存在浏览器中，服务器不需要做状态管理。
- 更容易`防范CSRF攻击`，因为在请求头中添加localStorage或sessionStorage中的token必须靠JavaScript代码完成，而不是自动添加到请求头中的。
- 可以防伪造和篡改，因为JWT有签名，伪造和篡改的令牌无法通过签名验证，会被认定是无效的令牌

当然，任何技术不可能只有优点没有缺点，JWT也有诸多缺点，大家需要在使用的时候引起注意，具体包括：

- 可能会遭受到XSS攻击（跨站脚本攻击），通过注入恶意脚本执行JavaScript代码获取到用户令牌。
- 在令牌过期之前，无法作废已经颁发的令牌，要解决这个问题，还需要额外的中间层和代码来辅助。
- JWT是用户的身份令牌，一旦泄露，任何人都可以获得该用户的所有权限。为了降低令牌被盗用后产生的风险，JWT的有效期应该设置得比较短。对于一些比较重要的权限，使用时应通过其他方式再次对用户进行认证，例如短信验证码等。

**基于token的用户跟踪具体流程如下**:

1. 用户登录时，如果登录成功就按照某种方式为用户生成一个令牌（token），该令牌中通常包含了用户标识、过期时间等信息而且需要加密并生成指纹（避免伪造或篡改令牌），服务器将令牌返回给前端；
2. 前端获取到服务器返回的token，保存在浏览器本地存储中（可以保存在localStorage或sessionStorage中，对于使用Vue.js的前端项目来说，还可以通过Vuex进行状态管理）；
3. 对于使用了前端路由的项目来说，前端每次路由跳转，可以先判断localStorage中有无token，如果没有则跳转到登录页；
4.每次请求后端数据接口，在HTTP请求头里携带token；后端接口判断请求头有无token，如果没有token以及token是无效的或过期的，服务器统一返回401；
4. 如果前端收到HTTP响应状态码401，则重定向到登录页面。
