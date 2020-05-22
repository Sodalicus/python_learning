" git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
" To install Vundle

set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'morhetz/gruvbox' " run :PluginInstall after this one, then the next line
autocmd vimenter * colorscheme gruvbox " After the above

Plugin 'davidhalter/jedi-vim' " autocompletion

Plugin 'preservim/nerdtree' " file system explorer
map <C-n> :NERDTreeToggle<CR>

call vundle#end()            " required
filetype plugin indent on    " required
" End of Vundle configuration
"
"set t_Co=256

set hidden " buffers option, lets you switch buffers without saving them

set termguicolors " support for true colors terminal

set number " show line numbers

set ts=4 " set tabs to have 4 spaces

set softtabstop=4 " number of spaces in tab when editing

set autoindent " indent when moving to the next line while writing code

set expandtab " expand tabs into spaces

set shiftwidth=4 " when using the >> or << commands, shift lines by 4 spaces

"set cursorline " show a visual line under the cursor's current line

set showmatch " show the matching part of the pair for [] {} and ()

set foldmethod=indent " folf based in indent level 
set foldlevel=99 " max fold level?
set foldlevelstart=10   " open most folds by default
set foldnestmax=10      " 10 nested fold max
set foldenable          " enable folding

set showcmd " show command in bottom bar

set incsearch           " search as characters are entered

set hlsearch            " highlight matches

let python_highlight_all = 1 " enable all Python syntax highlighting features

" Map F9 to run python script
autocmd FileType python map <buffer> <F9> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F9> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>

" colorscheme elflord " color theme, duh

nnoremap <space> za " Enable folding with the spacebar

syntax enable " enable syntax highlighting
