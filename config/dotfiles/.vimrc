"设置行号"
set number
"显示当前行号和列号"
set ruler

"设置语法高亮"
syntax enable
syntax on

set wildmenu
set encoding=utf-8
set cursorline

"配色方案"
"colorscheme desert"
"colorscheme default"
colorscheme industry

"设置字不会超出当前窗口"
set wrap

"设置tab键为4个空格"
set tabstop=4

"设置鼠标能够使用"
set mouse=a
set selection=exclusive
set selectmode=mouse,key

"设置自动缩进"
set autoindent

"设置搜索高亮"
set hls

"检测文件"
"filetype on"
"启动智能补全"
"filetype plugin indent on"

"绑定S键为快捷键"
map S :wq<CR>
map Q :q<CR>

"设置括号自动补全"
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap < <><ESC>i

"绑定目录树"
