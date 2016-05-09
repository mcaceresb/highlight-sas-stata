program define excellentProgram
version 14.0

local hi  = `1'
local bye = `2'
local yes = ln(`hi')

* This is a comment
set obs `= _N + 1'
gen neg = 1 - 1 / (1 + exp(score))

/*
 * Multi line comments are pretty
 * because they span many lines
 */

reg y x
xi: reg y2 x i.dummy // This is another comment type

di "This is a normal string with a `local' $global ${global}"
di `"This is a "super string" that takes on anything"'
di "string`1'two${three}" bad `"string " "' good `"string " "'

// This also works at line starts
adopath ++ "${lib}/code/ado/"
cap adopath - SITE
cap adopath - PLUS
/*cap adopath - PERSONAL
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
