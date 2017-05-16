<!DOCTYPE>
<html lang="zh-CN">
<head>
<title>Search Result</title>
<meta charset="UTF-8">
<link rel="shortcut icon" type="image/vnd.microsoft.icon" href="http://www.personalwebhhf.cn/favicon.ico">
<title>STUDY</title>
<link type="text/css" rel="stylesheet" href="http://www.personalwebhhf.cn/CSS/blogbase.css" />

<meta name="viewport" content="width=device-width minimum-scale=1.0 maximum-scale=1.0">
</head>
<body >
  <div id="header"> 
	  <h1 class="blogtitle_decorate">STUDY AND TRYING</h1>
	  <h3 class="descrption_title">For man is man and master of his fate.</h3>   
  </div> <!--end header-->
	<div id="nav" >  
	 <p>Search Result</p>
    	</div> 
   <div id="mainbody">
	<?php

	$Key_Words = $_POST['Key_Words'];
	if (!empty($Key_Words))
	{
		//echo $Key_Words."<br>";
        	$Para = array();
		$cmd = 'python PageRank.py  '.$Key_Words;
        	exec($cmd, $Para,$ret);
		$Len = count($Para);
		$i = 1;
		foreach ($Para as $url)
		{
			$Title =array();
			$CMD = 'python Loadhtml.py '.$url.' '.$Key_Words;
			$Key_Len = strlen($Key_Words);
			exec($CMD,$Title,$ret);
			echo "<div><a style='font-size:28px; font-family:KaiTi;'; href= $url>$Title[0]</a><div>";
			echo "<p>   <p>";
			$Str = strchr($Title[1],$Key_Words,true);
			echo $Str;
			echo "<span style= 'color:red';>$Key_Words</span>";
			$Str2 = strstr($Title[1],$Key_Words);
			$Str2 = substr($Str2,$Key_Len);
			echo "$Str2 .....  <a href= $url>more</a>";
			echo "<HR style='FILTER: alpha(opacity=100,finishopacity=0,style=2)' width='100%' color=#987cb9 SIZE=10>";
			
		}

	}
	else
	{
		echo "Key_Words is empty";
	}
	?>
   </div>
  <div class="footer" style="clear:both">
   <p class="copyright">Copyright@2016 hhf</p>
  </div>
</body>
</html>			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  
			  


