" ----------------------------------------------------------------------------
" Program: tex_fenced.vim
" Author:  github.com/mcaceresb
" Created: Sat May  7 19:23:06 EDT 2016
" Updated: Sun May  8 21:21:07 EDT 2016
" Purpose: Nested highlighting in LaTeX with minted and listings

" ---------------------------------------------------------------------
" Based on Tim Pope's vim-markdown (https://github.com/tpope/vim-markdown)

" Get list of fenced languages Vim knows about
if !exists("g:TeX_fenced_path")
    let g:TeX_fenced_path = $VIMRUNTIME . '/syntax/'
endif

let g:TeX_fenced_str  = globpath(g:TeX_fenced_path, '*.vim')
let g:TeX_fenced_str  = substitute(g:TeX_fenced_str, g:TeX_fenced_path, '','g')
let g:TeX_fenced_str  = substitute(g:TeX_fenced_str, '\.vim', '','g')
let g:TeX_fenced_available = split(g:TeX_fenced_str, '\n')
unlet! g:TeX_fenced_str

" Arbitrary list of languages if none specified
if !exists("g:TeX_fenced_languages")
    let g:TeX_fenced_languages = [
                \ 'css', 'diff', 'html', 'javascript', 'markdown', 'python',
                \ 'r', 'SAS=sas', 'sas', 'sh', 'sql', 'Stata=stata', 'stata',
                \ ]
endif

" Include them in the syntax definition
let s:done_include = {}
let g:TeX_fenced_groups = ''
for s:type in map(copy(g:TeX_fenced_languages), 'matchstr(v:val,"[^=]*$")')
    if index(g:TeX_fenced_available,  matchstr(s:type, '[^.]*')) < 0
        echo "Language '" . s:type . "' not found in " . g:TeX_fenced_path
        continue
    endif
    if has_key(s:done_include, matchstr(s:type,'[^.]*'))
        continue
    endif
    if s:type =~ '\.'
        let b:{matchstr(s:type,'[^.]*')}_subtype = matchstr(s:type,'\.\zs.*')
    endif
    exe 'syn include @TeXHighlight' .
                \ substitute(s:type,'\.','','g').
                \ ' syntax/' . matchstr(s:type,'[^.]*').'.vim'
    let g:TeX_fenced_groups = g:TeX_fenced_groups .
                \ ',TeXHighlight'.substitute(s:type,'\.','','g')
    unlet! b:current_syntax
    let s:done_include[matchstr(s:type,'[^.]*')] = 1
endfor
unlet! s:type
unlet! s:done_include

" Create a region for them within minted and listings
let s:done_include = {}
for s:type in g:TeX_fenced_languages
    if has_key(s:done_include, matchstr(s:type,'[^.]*'))
        continue
    endif
    exe 'syn region TeXHighlight' .
                \ substitute(matchstr(s:type,'[^=]*$'),'\..*','','') .
                \ ' matchgroup=texStatement start="^\s*\\begin{minted}.*{' .
                \ matchstr(s:type,'[^=]*') .
                \ '}.*$" end="^\s*\\end{minted}.*$" keepend contains=@TeXHighlight' .
                \ substitute(matchstr(s:type,'[^=]*$'),'\.','','g')
    exe 'syn region TeXHighlight' .
                \ substitute(matchstr(s:type,'[^=]*$'),'\..*','','') .
                \ ' matchgroup=texStatement start="^\s*\\begin{lstlisting}.*language\s*=\s*' .
                \ matchstr(s:type,'[^=]*') .
                \ '[,\]\s].*$" end="^\s*\\end{lstlisting}.*$" keepend contains=@TeXHighlight' .
                \ substitute(matchstr(s:type,'[^=]*$'),'\.','','g')
    let s:done_include[matchstr(s:type,'[^.]*')] = 1
endfor

" ---------------------------------------------------------------------
" Re-run TeX zones so it accepts the new groups (from syntax/tex.vim)

if !exists("g:tex_fold_enabled")
    let s:tex_fold_enabled= 0
elseif g:tex_fold_enabled && !has("folding")
    let s:tex_fold_enabled= 0
    echomsg "Ignoring g:tex_fold_enabled=" .  g:tex_fold_enabled .
                \ "; need to re-compile vim for +fold support"
else
    let s:tex_fold_enabled= 1
endif

if s:tex_fold_enabled && has("folding")
    com! -nargs=* TexFold <args> fold
else
    com! -nargs=* TexFold <args>
endif

if exists("g:tex_nospell") && g:tex_nospell
    let s:tex_nospell = 1
else
    let s:tex_nospell = 0
endif

exe 'syn cluster texFoldGroup contains=texAccent,texBadMath,texComment,texDefCmd,texDelimiter,texDocType,texInput,texInputFile,texLength,texLigature,texMatcher,texMathZoneV,texMathZoneW,texMathZoneX,texMathZoneY,texMathZoneZ,texNewCmd,texNewEnv,texOnlyMath,texOption,texParen,texRefZone,texSection,texBeginEnd,texSectionZone,texSpaceCode,texSpecialChar,texStatement,texString,texTypeSize,texTypeStyle,texZone,@texMathZones,texTitle,texAbstract,texBoldStyle,texItalStyle,texNoSpell' . g:TeX_fenced_groups

if !s:tex_nospell
    TexFold syn region texDocZone
                \ matchgroup=texSection
                \ start='\\begin\s*{\s*document\s*}'
                \ end='\\end\s*{\s*document\s*}'
                \ contains=@texFoldGroup,@texDocGroup,@Spell
else
    TexFold syn region texDocZone
                \ matchgroup=texSection
                \ start='\\begin\s*{\s*document\s*}'
                \ end='\\end\s*{\s*document\s*}'
                \ contains=@texFoldGroup,@texDocGroup
endif
