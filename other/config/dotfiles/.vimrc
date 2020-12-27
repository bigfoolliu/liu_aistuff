" Configuration file for vim

"*************************vundle插件管理配置***********************

" 表明不与Vi兼容，因为如果与Vi兼容，很多强大的功能无法使用
set nocompatible              " be iMproved, required
filetype off                  " required


" 配置f5键执行.py脚本, 加载文件类型插件功能
" To ignore plugin indent changes, instead use:
filetype plugin on
map <F5> :call PRUN()<CR>
func! PRUN()
    exec "w"
    if &filetype == 'python'
        exec "!python %"
    endif
endfunc


" 方向键不能使用设置
" set term=builtin_ansi

" running time path 的缩写，即我们到哪里去找插件
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'

" 不同形式的插件支持方式，各种形式的Plugin一定要在begin/end之间


" github上的插件，只需要写用户名和仓库名即可
" Plugin 'tpope/vim-fugitive'
Plugin 'preservim/nerdtree'

" 文件结构插件，比如展示当前文件的类和函数等
Plugin 'majutsushi/tagbar'

" markdown插件
Plugin 'godlygeek/tabular' "必要插件，安装在vim-markdown前面
Plugin 'plasticboy/vim-markdown'
Plugin 'mzlogin/vim-markdown-toc'

" markdown预览插件,(映射F8和F9键预览)
Plugin 'iamcco/mathjax-support-for-mkdp'
Plugin 'iamcco/markdown-preview.vim'


" 代码片段插Plugin 'SirVer/ultisnips'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'


" 多选可视插件
" select words with Ctrl-N (like Ctrl-d in Sublime Text/VS Code)
" create cursors vertically with Ctrl-Down/Ctrl-Up
" select one character at a time with Shift-Arrows
" press n/N to get next/previous occurrence
" press [/] to select next/previous cursor
" press q to skip current and get next occurrence
" press Q to remove current cursor/selection
" start insert mode with i,a,I,A
Plugin 'mg979/vim-visual-multi', {'branch': 'master'}


" python使用插件
" Plugin 'klen/python-mode'                   " Python mode (docs, refactor, lints...)
" Plugin 'scrooloose/syntastic'               " Syntax checking plugin for Vim
" Plugin 'davidhalter/jedi-vim'

" python补全插件
Plugin 'davidhalter/jedi-vim'

" Plugin 'vim-airline'


" 代码补全插件
" Plugin 'Valloric/YouCompleteMe'

" vim-scriptes网站上插件，直接写名字即可
" Plugin 'L9'

" 也是git仓库，但是不是Github上的插件，比如公司内的git仓库
" Plugin 'git://git.wincent.com/command-t.git'

" 本地的插件（自己使用的）
" Plugin 'file:///home/gmarik/path/to/plugin'

" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
" Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}


" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}


" 所有的插件安装必须在此之前
call vundle#end()            " required
filetype plugin indent on    " required

"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
"******************************************************************


set modelines=0		" CVE-2007-2438

" Normally we use vim-extensions. If you want true vi-compatibility
" remove change the following statements
set nocompatible	" Use Vim defaults instead of 100% vi compatibility
set backspace=2		" more powerful backspacing

" Don't write backup file if vim is being called by "crontab -e"
au BufWrite /private/tmp/crontab.* set nowritebackup nobackup
" Don't write backup file if vim is being called by "chpass"
au BufWrite /private/etc/pw.* set nowritebackup nobackup

let skip_defaults_vim=1


"***************************基本配置*********************************

set fileformats=unix,dos

"设置行号
set number

"启用256色
set t_Co=256

"设置当前行号和列号
set ruler

"显示光标当前行行号，其他行为相对
set relativenumber

"设置文字不会超出当前窗口
set wrap

"**********搜索配置**********

"设置搜索结果高亮
set hls

"设置忽略大小写
set ignorecase

"搜索时，每输入一个词，跳到第一个匹配结果
set incsearch

"打开语法亮度
syntax enable

"底部显示当前模式
set showmode

"打开文件类型自动检测
syntax on

"设置状态栏显示,0:不显示，1:只在多窗口显示，2:总是显示
set laststatus=2

"设置tab键的空格位数
"设置自动缩进
set ts=4
set expandtab
set autoindent


"设置和系统共用剪贴板
set clipboard+=unnamed

"设置括号自动补全"
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap < <><ESC>i

"命令模式下，底部按tab可以提示补全
"第一次按下会返回所有结果，第二次依次选择结果
set wildmenu
set wildmode=longest:list,full

"*********************光标配置***************************
"设置不同模式下的光标
let &t_SI.="\e[5 q" "SI = INSERT mode
let &t_SR.="\e[4 q" "SR = REPLACE mode
let &t_EI.="\e[1 q" "EI = NORMAL mode (ELSE)

"光标对应模式
"  1 -> blinking block
"  2 -> solid block
"  3 -> blinking underscore
"  4 -> solid underscore
"  5 -> blinking vertical bar
"  6 -> solid vertical bar

let &t_SI = "\<Esc>]50;CursorShape=1\x7"
let &t_SR = "\<Esc>]50;CursorShape=2\x7"
let &t_EI = "\<Esc>]50;CursorShape=0\x7"

"设置光标高亮行
set cursorline


"************************快捷键配置*********************************
"将C映射为 "+y ，快速复制选中的内容复制到系统剪贴板
map C "+y


" 映射移动行，按下'2]e'就可以将当前行快速下移两行，'2[e'就可将当前行快速上移2行
nnoremap [e :<c-u>execute 'move -1-'. v:count1<cr>
nnoremap ]e :<c-u>execute 'move +'. v:count1<cr>

" 移动到当前行的行尾，不包括换行符
nnoremap L g_

"**************************NERDTree配置*********************************

"使用F2键快速调出和隐藏它
map <F2> :NERDTreeToggle<CR>

" 关闭vim时，如果打开的文件除了NERDTree没有其他文件时，它自动关闭，减少多次按:q!
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif


" 忽略以下文件的显示
let NERDTreeIgnore=['\.pyc','\~$','\.swp']

" 显示书签列表
let NERDTreeShowBookmarks=1

" 显示隐藏文件
let NERDTreeShowHidden=1

" 目录树窗口尺寸
let g:NERDTreeWinSize = 40


" 显示行号
let NERDTreeShowLineNumbers = 1
let NERDTreeAutoCenter = 1

" 在终端启动vim时，共享NERDTree
" let g:nerdtree_tabs_open_on_console_startup = 1


"**************************tagbar配置*********************************

" F6键映射展示当前文件结构
nmap <F6> :TagbarToggle<CR>


"**************************vimairline配置*********************************

let g:airline#extensions#tabline#enabled = 1


"**************************vim-markdown配置*********************************

" 高亮数学公式
let g:vim_markdown_math = 1

" 配置F3键盘快速调用出markdown文件toc
map <F3> :Toc<CR>

" 禁止折叠
let g:vim_markdown_folding_disabled = 1

" 映射markdown预览快捷键
nmap <silent> <F8> <Plug>MarkdownPreview
imap <silent> <F8> <Plug>MarkdownPreview
nmap <silent> <F9> <Plug>StopMarkdownPreview
imap <silent> <F9> <Plug>StopMarkdownPreview

"************************vim-markdown-toc配置*********************************

" 自动更新已经存在的toc
let g:vmt_auto_update_on_save = 1

" Table of Contents 项目前面的标记默认全都是 *，修改为根据级别循环使用 *、- 和 +
let g:vmt_cycle_list_item_markers = 1

"*****************************ultisnips配置***********************************

" 使用tab作为触发的键
let g:UltiSnipsExpandTrigger="<tab>"

let g:UltiSnipsJumpForwardTrigger="<c-b>"

let g:UltiSnipsJumpBackwardTrigger="<c-z>"


"*****************************jedivim配置************************************

let g:jedi#completions_command = "<C-N>"  " ctrl+N设置快捷键自动补全


