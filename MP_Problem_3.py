#MP3-Python
import numpy as np
import ast
def Convert(string):
    arrlst = ast.literal_eval(string)
    arr = np.asarray(arrlst)
    print(len(arr))
    xi = arr[0:(len(arr)),0]
    yi = arr[0:(len(arr)),1]
    for n in range(1,len(arr)):
        if n <=10:
            pfit = np.polyfit(xi,yi,n)
            polft.append(pfit)
            
            pval = np.polyval(pfit,xi) 
            polval.append(pval)
            
            norm = np.linalg.norm(yi-pval) #finding the norm
            errorvector.append(norm)
            
            lne = np.min(norm) #finding the least-norm error vector
            lnerror.append(lne)
        elif n >10:
            raise Exception('Sorry. Only polinomials until 10th degree are accepted.')
    print('Coefficients of the Polynomial: \n',pval,'\n')
    print('Least-Norm Error Vector,e(x): \n',lne,'\n')
polft = []
polval = []
errorvector=[]
lnerror=[]
arrstr = input('Enter array(Form: [[x1,y1],...[xn,yn]])\nNote: Please limit it to the 10th Degree only.: ') 
Convert(arrstr)
