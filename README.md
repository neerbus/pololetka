# pololetka


1. set up programu

  aby tento script fungoval, musi byt upraven na dvou mistech. tyto mista jsou prvni dva radky. mezi pomlcky je potreba doplnit lokaci odpovidajich souboru.
  jestli nevite jak se ziskava lokace programu -> https://www.youtube.com/watch?v=MVoQhYWJuvw . bohuzel tato lokace se zkopiruje s "\" a ne s "/". python
  spatne reaguje na "\" ve stringu, protoze se pouziva napr. jako konec radku ve slove, proto musite zmenit "\" na "/", aby program fungoval. po zadani lokaci
  souboru by program mel normalne fungovat.

2. jak funguje?
   
  v programu si muzete vybrat obdobi a obtiznost nebo mod pololetky, ktery obsahuje pouze autory, kteri budou v pololetce a jine otazky, ktere muzou byt v testu.
  tyto otazky se deli na autory, vyber spravne znaky neceho a ano/ne otazky. u obdobich jsou pouze autori z daneho obdobi a jsou bud lehke nebo tezke (podle vybrane
  obtiznosti). 
  U autoru jsou 3 informace + zeme puvodu. v lehke obtiznosti je pouze jedna z techto obtiznosti skryta a v tezke jsou 2 + zeme puvodu skryte. ukolem je odpoved na
  skryte informace pomoci ostatnich. pololetka je automaticky v tezke obtiznosti. u "vyber spravne znaky" otazky program vypise 8 znaku. vasim ukolem je odpoved 
  pomoci cisel a postupne zleva do prava - např. prvni odpoved: 1, druha odpoved: 3 ... u ano/ne otazek staci napsat ane nebo ne.
  
3. syntax odpovedi

  1. odpovedi musi byt psane bez hacku a carek. specialni znaky mohou byt pouzity, ale jenom jedina odpoved vyzaduje jejich pouziti.
  2. pokud za odpovedy date mezeru nebo tam bude nejaka navic tak je to pocitane za chybu
  3. program je psany v malych pismenech, ale u odpovedi ignoruje velka mala.

