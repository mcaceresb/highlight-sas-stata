program define excellentProgram
version 14.0

local hi  = `1'
local bye = `2'
local yes = ln(`hi')

* This is a comment
set obs `= _N + 1'
gen neg = 1 - 1 / (1 + exp(score))
bysort group: egen pos = sum(abs(neg))

/*
 * Multi line comments are pretty
 * because they span many lines
 */

reg y x if bool == 1
xi: reg y2 x i.dummy // This is another comment type
matrix list `r(table)'
levelsof x
disp `"`r(levels)'"'

di "This is a normal string with a `local' $global ${global}"
di "Nested: $`=expression'glo${glo`loc`:extended macro'al'bal}bal"
di "Escape: \$100 or \`local\`"
di `"This is a "super string" that takes on anything"'
di "string`1'two${three}" bad `"string " "' good `"string " "'

global HelloThisIsAVeryLengthyGlobalYes 23
local RandomLocalAlsoVeryLongName ThisIsAVeryLengthyGlobal
disp "${Hello`RandomLocalAlsoVeryLongName'Yes}"
disp %21.0gc _N

// This also works at line starts
adopath ++ "${lib}/code/ado/"
cap adopath - SITE
cap adopath - PLUS
/*cap adopath - PERSONAL
/*Nested*/
cap adopath - OLDPLACE*/

forval i = 1 / 4{
  cap reg y x`i', robust
  if `i' == 2 {
    local c = _b[_cons]
    local b = _b[x`i']
    local x = ln(`i')
  }
}

* Something about how mata is really a second language within Stata
mata: mata mlib index
end
