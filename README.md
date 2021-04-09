<h1>sqlmap PHPSESSID Bypass Tamper</h1>
<p>sqlmap random PHPSESSID | PHPSESSION protection &amp;&amp; block bypass</p>

<h4>EN</h4>
<h3>Usage:</h3>
<p> Put the randomsessid.py in the tamper folder of the directory where sqlmap is located.</p>
<code>sqlmap -r xx.txt --tamper=randomsessid.py</code>

<p>Some sites create a block while testing and keep it as a session. I encountered this situation while testing with sqlmap and wrote a tamper.</p>
<p>this tamper generates a random PHPSESSID and sends it as a cookie. In this way, it creates the impression of a new login and overcomes the obstacle.</p>
<h4>TR</h4>
<h3>Usage:</h3>
<p>  randomsessid.py adlı dosyayı sqlmap'in bulunduğu konumda ki tamper klasörüne atın.</p>

<code>sqlmap -r xx.txt --tamper=randomsessid.py</code>

<p>bu tamper rastgele bir PHPSESSID oluşturur ve bunu bir cookie bilgisi olarak gönderir. Bu şekilde yeni bir giriş izlenimi yaratır ve engeli aşar.</p>
<p>Coded by LQM33</p>
