clear all

set more off

/////////////////////////////////////////////////////////
/* Define paths */
global dir "C:\Users\estca\OneDrive\Documentos\Github\macro-seminar"

global data "$dir/data"

global output "$dir/output"

/////////////////////////////////////////////////////////
/* Install packages */
ssc install outreg2
ssc install estout

/////////////////////////////////////////////////////////
///////////////////// Peru //////////////////////////////

/*** 1. Import the file and prepare the data ***/ 

import excel using "$data/peru.xlsx", describe

clear all

import excel using "$data/peru.xlsx", firstrow

codebook , c

/*** 2. Run OLS and IV regressions ***/ 

reg CPI CBI Unemploymentrate, robust
outreg2 using "$output/ols_peru.doc", replace ctitle(OLS)

margins, dydx(CBI Unemploymentrate)
estimates store reg_ols_peru

ivreg2 CPI (CBI = Currentaccountbalance) Unemploymentrate
outreg2 using "$output/iv_peru.doc", append ctitle(IV)
mfx 
estimates store reg_iv_peru

/*** 3. Display the results in a table ***/

estimates table reg_ols_peru reg_iv_peru ,star(.1 .05 .01)

////////////////////////////////////////////////////////
///////////////////// Chile ////////////////////////////

clear

/*** 1. Import the file and prepare the data ***/ 

import excel using "$data/chile.xlsx", firstrow

codebook , c

/*** 2. Perform OLS and IV regressions ***/

reg CPI CBI Unemploymentrate, robust
outreg2 using "$output/ols_chile.doc", replace ctitle(OLS)

margins, dydx(CBI Unemploymentrate)
estimates store reg_ols_chile

ivreg2 CPI (CBI = Currentaccountbalance) Unemploymentrate
outreg2 using "$output/iv_chile.doc", append ctitle(IV)

mfx 
estimates store reg_iv_chile

/*** 3. Display the results in a table ***/

estimates table reg_ols_chile reg_iv_chile ,star(.1 .05 .01)

////////////////////////////////////////////////////////
///////////////////// Colombia /////////////////////////

clear

/*** 1. Import the file and prepare the data ***/ 

import excel using "$data/colombia.xlsx", firstrow

codebook , c

/*** 2. Perform OLS and IV regressions ***/

reg CPI CBI Unemploymentrate, robust
outreg2 using "$output/ols_colombia.doc", replace ctitle(OLS)

margins, dydx(CBI Unemploymentrate)
estimates store reg_ols_colombia

ivreg2 CPI (CBI = Currentaccountbalance) Unemploymentrate
outreg2 using "$output/iv_colombia.doc", append ctitle(IV)

mfx 
estimates store reg_iv_colombia

/*** 3. Display the results in a table ***/

estimates table reg_ols_colombia reg_iv_colombia ,star(.1 .05 .01)

////////////////////////////////////////////////////////
///////////////////// Mexico ///////////////////////////

clear

/*** 1. Import the file and prepare the data ***/ 

import excel using "$data/mexico.xlsx", firstrow

codebook , c

/*** 2. Perform OLS and IV regressions ***/

reg CPI CBI Unemploymentrate, robust
outreg2 using "$output/ols_mexico.doc", replace ctitle(OLS)

margins, dydx(CBI Unemploymentrate)
estimates store reg_ols_mexico

ivreg2 CPI (CBI = Currentaccountbalance) Unemploymentrate
outreg2 using "$output/iv_mexico.doc", append ctitle(IV)

mfx 
estimates store reg_iv_mexico

/*** 3. Display the results in a table ***/

estimates table reg_ols_mexico reg_iv_mexico ,star(.1 .05 .01)

////////////////////////////////////////////////////////
/////////////////// Pacific Alliance ///////////////////

/*** OLS regressions ***/ 

estimates table reg_ols_peru reg_ols_chile reg_ols_colombia reg_ols_mexico ,star(.1 .05 .01)

/*** IV regressions ***/ 

estimates table reg_iv_peru reg_iv_chile reg_iv_colombia reg_iv_mexico ,star(.1 .05 .01)

