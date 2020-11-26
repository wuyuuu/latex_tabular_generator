# latex_tabular_generator

## Run script
```
python main.py --input input.txt --output output.txt
```
### Input is like
```
title
col1 , col2, col3
name1, data1, data2
name2, data2, data3
```
### Then output would be like
```
\begin{table}
\begin{tabular} {|p{3cm}|p{3cm}|p{3cm}|}
\hline
\multicolumn{3}{|c|}{title}\\
\hline
col1 & col2& col3\\
\hline
name1& data1& data2\\
name2& data2& data3\\
\hline
\end{tabular}
\end{table}
```
