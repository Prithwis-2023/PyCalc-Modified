
def ADD(A,B):
    return A+B
def SUBSTRACT(A,B):
    return A-B
def MULTIPLY(A,B):
    return A*B
def QUOTIENT_OF_DIVISION(A,B):
    return A//B
def REMAINDER_OF_DIVISION(A,B):
    return A%B
def AVERAGE(A,B):
    return (A+B)/2
def N_ROOT(A,B):
    return (A)**(1/B)
def POWER(A,B):
    return (A)**(B)
def COMPOSE(f,g):
    return lambda x : f(g(x))
print("WELCOME TO PyCalc")
print("HERE YOU CAN DO BASIC ARITHMETIC OPERATIONS AND MANY MORE!")
print("REMEMBER THE FOLLOWING KEYWORDS:")
print("ADD(A,B): FOR ADDING A AND B.")
print("SUBSTRACT(A,B): FOR SUBSTRACTING B FROM A.")
print("MULTIPLY(A,B): FOR MULTIPLYING A AND B.")
print("SQRT(A): FOR SQUARE ROOT.")
print("POWER(A,B): FOR A^B.")
print("AVERAGE(A,B): FOR AVERAGE OF A AND B.")
print("QUOTIENT_OF_DIVISION(A,B): QUOTIENT WHEN A IS DIVIDED BY B.")
print("REMAINDER_OF_DIVISION(A,B): REMAINDER WHEN A IS DIVIDED BY B.")
print("exp() : EULER'S NUMBER.")
print("A KIND REQUEST:PLEASE DO NOT USE THE COMPOSITIO FOR GRAPHS. IT'S STILL UNDER PROCESSING STAGE! ")
print("PLEASE SELECT FROM FOLLOWING OPERATIONS:")
print("ADD\nSUBSTRACT\nMULTIPLY\nQUOTIENT_OF_DIVISION\nREMAINDER_OF_DIVISION\nAVERAGE\nN_ROOT\nPOWER\nPARTITIONS\nFINDING_ROOTS\nLOGARITHMIC_OPERATIONS\nGRAPHS\nCALCULUS\nPRIME_IDENTIFICATION\n2_BY_2_PARTITIONS\nCOMBINATORIAL_CALCULATIONS\nFUN_ZONE")
E = input("ENTER THE OPERATION YOU NEED:")


if E == "ADD":
    w = int(input("HOW MANY TIMES YOU WANT TO ADD 2 NUMBERS:"))
    for i in range (w):
     A=int(input("ENTER THE FIRST NUMBER:"))
     B=int(input("ENTER THE SECOND NUMBER:"))
     print(ADD(A,B))
    i=i+1 
elif E == "SUBSTRACT":
    w = int(input("HOW MANY TIMES YOU WANT TO SUBSTRACT 2 NUMBERS:"))
    for i in range (w):
     A=int(input("ENTER THE FIRST NUMBER:"))
     B=int(input("ENTER THE SECOND NUMBER:"))
     print(SUBSTRACT(A,B))
    i=i+1 
elif E == "MULTIPLY":
    w = int(input("HOW MANY TIMES YOU WANT TO MULTIPLY 2 NUMBERS:"))
    for i in range (w):
     A=int(input("ENTER THE FIRST NUMBER:"))
     B=int(input("ENTER THE SECOND NUMBER:"))
     print(MULTIPLY(A,B))
    i=i+1 
elif E == "QUOTIENT_OF_DIVISION":
    w = int(input("HOW MANY TIMES YOU WANT TO FIND THE QUOTIENT OF A DIVISION OF 2 NUMBERS:"))
    for i in range (w):
     A=int(input("ENTER THE FIRST NUMBER:"))
     B=int(input("ENTER THE SECOND NUMBER:"))
     print(QUOTIENT_OF_DIVISION(A,B))
    i=i+1 
elif E == "REMAINDER_OF_DIVISION":
    A=int(input("ENTER THE FIRST NUMBER:"))
    B=int(input("ENTER THE SECOND NUMBER:"))
    print(REMAINDER_OF_DIVISION(A,B))
elif E == "AVERAGE":
    A=int(input("ENTER THE FIRST NUMBER:"))
    B=int(input("ENTER THE SECOND NUMBER:"))
    print(AVERAGE(A,B))
elif E == "PARTITIONS":
    w=int(input("ENTER THE NUMBER:"))
    X=1/((4*w*3**(1/2))*(2.718)**(3.414*((2*w)/3)**(1/2)))
    print(X)
elif E == "FINDING_ROOTS":
    V=int(input("ENTER THE DEGREE OF THE POLYNOMIAL:"))
    if V == 2:
        Y=int(input("ENTER THE COEFFICIENT OF X^2:"))
        Z=int(input("ENTER THE COEFFICIENT OF X:"))
        W=int(input("ENTER THE CONSTANT:"))
        T=(-Z+((Z**2)-4*Y*W)**(1/2))/(2*Y)
        U=(-Z-((Z**2)-4*Y*W)**(1/2))/(2*Y)
        print("THE POLYNOMIAL IS ({}X^2) + ({}X) + ({})".format(Y,Z,W))
        print("THE FIRST ROOT IS",T)
        print("THE SECOND ROOT IS",U)
    else:
        print("WE CURRENTLY DON'T SUPPORT POLYNOMIALS OF DEGREES MORE THAN 2")
elif E == "LOGARITHMIC_OPERATIONS":
    a=int(input("ENTER THE NUMBER:"))
    import math
    print(math.log(a))
elif E == "POWER":
    A=int(input("ENTER THE BASE:"))
    B=int(input("ENTER THE EXPONENT:"))
    print(POWER(A,B))
elif E == "N_ROOT":
    A=int(input("ENTER THE NUMBER:"))
    B=int(input("ENTER THE NUMBER N:"))
    print(N_ROOT(A,B))
        
        
elif E == "GRAPHS":
    print("TRIGONOMETRIC\nEXPONENTIAL\nLOGARITHMIC\nPOLYNOMIAL\nCOMPOSITION")
    d=input("PLEASE ENTER WHICH TYPE OF GRAPH YOU HAVE TO MAKE:")
    if d == "TRIGONOMETRIC":
         b=input("ENTER THE TRIGONONOMETRIC FUNCTION(sin/cos/tan):")
         c=float(input("ENTER THE NUMBER WHICH WILL BE COEFICIENT OF theta:"))
         if b == "sin":
          import matplotlib.pyplot as plt
          import numpy as np
          x=np.arange(0, c*(np.pi), 0.1)
          y=np.sin(x)
          plt.plot(x,y)
          plt.show()
         elif b == "cos":
          import matplotlib.pyplot as plt
          import numpy as np
          x=np.arange(0, c*(np.pi), 0.1)
          y=np.cos(x)
          plt.plot(x,y)
          plt.show()
         elif b == "tan":
          import matplotlib.pyplot as plt
          import numpy as np
          x=np.arange(0, c*(np.pi), 0.1)
          y=np.tan(x)
          plt.plot(x,y)
          plt.show()
         elif b == "cosec":
          import matplotlib.pyplot as plt
          import numpy as np
          x=np.arange(0, c*(np.pi), 0.1)
          y=np.csc(x)
          plt.plot(x,y)
          plt.show()
         elif b == "sec":
          import matplotlib.pyplot as plt
          import numpy as np
          x=np.arange(0, c*(np.pi), 0.1)
          y=np.sec(x)
          plt.plot(x,y)
          plt.show()
         elif b == "cot":
          import matplotlib.pyplot as plt
          import numpy as np
          x=np.arange(0, c*(np.pi), 0.1)
          y=np.cot(x)
          plt.plot(x,y)
          plt.show()
         else:
          print("INVALID INPUT")
    elif d == "EXPONENTIAL":
        f=int(input("ENTER THE FIRST VALUE OF RANGE:"))
        g=int(input("ENTER THE LAST VALUE OF RANGE:" ))
        e=2.718281828
        import matplotlib.pyplot as plt
        import numpy as np
        x=np.arange(f,g,0.1)
        y=np.e**x
        plt.plot(x,y)
        plt.show()
    elif d == "LOGARITHMIC":
        import matplotlib.pyplot as plt
        import numpy as np
        h=int(input("ENTER THE LOWER BOUND OF RANGE:"))
        i=int(input("ENTER THE UPPER BOUND OF RANGE:"))
        x=np.arange(h,i,0.1)
        y=np.log(x)
        plt.plot(x,y)
        plt.show()
    elif d == "POLYNOMIAL":
        a_y = input("ENTER WHAT TYPE OF POLYNOMIAL GRAPH(LINEAR/QUADRATIC/CUBIC/BIQUADRATIC):")
        if a_y == "LINEAR":
            import numpy as np
            import matplotlib.pyplot as plt
            a_e = int(input("ENTER THE COEFFICIENT OF X:"))
            a_f = int(input("ENTER THE CONSTANT:"))
            a_g=int(input("ENTER THE FIRST NUMBER IN THE RANGE:"))
            a_h=int(input("ENTER THE LAST NUMBER IN THE RANGE:"))
            x=np.linspace(a_g,a_h,256, endpoint=True)
            y=a_e*(x)+a_f
            plt.plot(x,y)
            plt.show()
        if a_y == "QUADRATIC":
            import numpy as np
            import matplotlib.pyplot as plt
            a_s=int(input("ENTER THE COEFFICIENT OF X^2:"))
            a_d=int(input("ENTER THE COEFFICIENT OF X:"))
            a_f=int(input("ENTER THE CONSTANT:"))
            a_g=int(input("ENTER THE FIRST NUMBER IN THE RANGE:"))
            a_h=int(input("ENTER THE LAST NUMBER IN THE RANGE:"))
            x=np.linspace(a_g,a_h,256, endpoint = True)
            y=(a_s*(x*x))+(a_d*x)+a_f
            plt.plot(x,y)
            plt.show()
        elif a_y == "CUBIC":
            import numpy as np
            import matplotlib.pyplot as plt
            a_q=int(input("ENTER THE COEFFICIENT OF X^3:"))
            a_s=int(input("ENTER THE COEFFICIENT OF X^2:"))
            a_d=int(input("ENTER THE COEFFICIENT OF X:"))
            a_f=int(input("ENTER THE CONSTANT:"))
            a_g=int(input("ENTER THE FIRST NUMBER IN THE RANGE:"))
            a_h=int(input("ENTER THE LAST NUMBER IN THE RANGE:"))
            x=np.linspace(a_g,a_h,256, endpoint = True)
            y=(a_q*(x*x*x))+(a_s*(x*x))+(a_d*x)+a_f
            plt.plot(x,y)
            plt.show()
        elif a_y == "BIQUADRATIC":
            import numpy as np
            import matplotlib.pyplot as plt
            a_r=int(input("ENTER THE COEFFICIENT OF X^4:"))
            a_q=int(input("ENTER THE COEFFICIENT OF X^3:"))
            a_s=int(input("ENTER THE COEFFICIENT OF X^2:"))
            a_d=int(input("ENTER THE COEFFICIENT OF X:"))
            a_f=int(input("ENTER THE CONSTANT:"))
            a_g=int(input("ENTER THE FIRST NUMBER IN THE RANGE:"))
            a_h=int(input("ENTER THE LAST NUMBER IN THE RANGE:"))
            x=np.linspace(a_g,a_h,256, endpoint = True)
            y=(a_r*(x*x*x*x))+(a_q*(x*x*x))+(a_s*(x*x))+(a_d*x)+a_f
            plt.plot(x,y)
            plt.show()
    elif d == "COMPOSITION":
        import numpy as np
        import matplotlib.pyplot as plt
        q_s =int(input("ENTER THE LOWER BOUND IN THE RANGE:"))
        t_i =int(input("ENTER THE UPPER BOUND IN THE RANGE:"))
        e_w = input("ENTER THE INNER FUNCTION:")
        w_e = input("ENTER THE OUTER FUNCTION:")
        x = np.linspace(q_s,t_i,0.1)
        y = COMPOSE(w_e, e_w)
        plt.plot(x,y)
        plt.show()
    else:
        print("INVALID INPUT")
elif E == "CALCULUS":
    k=input("DIFFERENTIATION/INTEGRATION:")
    if k == "DIFFERENTIATION":
        print("REMEMBER! IN OUTPUT THE FIRST EXPRESSION IS OF THE ACTUAL FUNCTION WHILE THE SECOND, THIRD, FOURTH CONTAINS THE FIRST DERIVATIVE, SECOND DERIVATIVE....and so on"  )
        print("COMPOSITION OF FUNCTIONS IS INBUILT")
        l=input("WHICH TYPE OF FUNCTION YOU WANT TO USE TRIGONOMETRIC,ALGEBRIC,LOGARITHMIC,EXPONENTIAL:")
        if l == "TRIGONOMETRIC":
            m = input("ENTER THE TRIGONOMETRIC FUNCTION(sin/cos/tan/cosec/sec/cot):")
            if m == "sin":
                n=input("ENTER THE FUNCTION WHICH WILL BE WITHIN SIN():")
                from sympy import *
                x,y,z = symbols('x y z')
                init_printing(use_unicode=True)
                k_l=diff(sin(n)),"(THE FIRST DERIVATIVE W.R.T x)"
                k_m=diff(diff(sin(n))),"(THE SECOND DERIVATIVE W.R.T x)"
                k_n=diff(diff(diff(sin(n)))),"(THE THIRD DERIVATIVE W.R.T x)"
                k_o=diff(diff(diff(diff(sin(n))))),"(THE FOURTH DERIVATIVE W.R.T x)"
                print(k_l)
                print(k_m)
                print(k_n)
                print(k_o)
                  
                
            elif m == "cos":
                o=input("ENTER THE FUNCTION WHICH WILL BE WITHIN COS():")
                from sympy import *
                x,y,z = symbols('x y z')
                init_printing(use_unicode=True)
                a_b=1
                for a_b in range(4):
                    j_k=(diff(cos(o)),x,a_b)
                    print(j_k)
                a_b=a_b+1    
                
            elif m == "tan":
                p=input("ENTER THE FUNCTION WHICH WILL BE WITHIN TAN():")
                from sympy import *
                x,y,z = symbols('x y z')  
                init_printing(use_unicode=True)
                a_b=1
                for a_b in range(4):
                    i_j=(diff(tan(p)),x,a_b)
                    print(i_j)
                a_b=a_b+1    
                
            elif m == "cosec":
                q=input("ENTER THE FUNCTION WHICH IS WITHIN COSEC():")
                from sympy import *
                x,y,z = symbols('x y z')  
                init_printing(use_unicode=True)
                a_b=1
                for a_b in range(4):
                    h_i=(diff(1/sin(q)),x,a_b)
                    print(h_i)
                a_b=a_b+1    
                
            elif m == "sec":
                r=input("ENTER THE FUNCTION WHICH WILL BE WITHIN SEC():")
                from sympy import *
                x,y,z = symbols('x y z')  
                init_printing(use_unicode=True)
                a_b=1
                for a_b in range(4):
                     g_h=(diff(1/cos(r)),x,a_b)
                     print(g_h)
                a_b=a_b+1    
                
            elif m == "cot":
                s=input("ENTER THE FUNCTION WHICH WILL BE WITHIN COT():")
                from sympy import *
                x,y,z = symbols('x y z')  
                init_printing(use_unicode=True)
                a_b=1
                for a_b in range(4):
                    f_g=(diff(1/tan(s)),x,a_b)
                    print(f_g)
                a_b=a_b+1    
                
            else:
                print("INVALID INPUT")
        elif l == "ALGEBRIC":
            t=input("ENTER THE ALGEBRIC EXPRESSION:")
            from sympy import *
            x,y,z = symbols('x y z')  
            init_printing(use_unicode=True)
            a_b=1
            for a_b in range(4):
                e_f=(diff(t),x,a_b)
                print(e_f)
            a_b=a_b+1    
        elif l == "LOGARITHMIC":
            u=input("ENTER THE FUNCTION WHICH WILL BE IN LOG():")
            from sympy import *
            x,y,z = symbols('x y z')  
            init_printing(use_unicode=True)
            a_b=1
            for a_b in range(4):
                c_d=(diff(log(u),x,a_b))
                print(c_d)
            a_b=a_b+1
        
            
        elif l == "EXPONENTIAL":
            v=input("ENTER THE FUNCTION WHICH WILL BE IN THE POWER OF e:")
            from sympy import *
            x,y,z = symbols('x y z')  
            init_printing(use_unicode=True)
            a_b=1
            for a_b in range(4):
                d_e=(diff(exp(v),x,a_b))
                print(d_e)
            a_b=a_b+1
        
            
        else:
            print("NOT SUPPORTED CURRENTLY")
    elif k == "INTEGRATION":
        
        
        
        w=input("WHICH TYPE OF FUNCTION YOU WANT TO USE (TRIGONOMETRIC,ALGEBRIC,LOGARITHMIC,EXPONENTIAL) :")
        if w == "ALGEBRIC":
            p_q = input("WHICH TYPE OF INTEGRAL DO YOU NEED(LINE/SURFACE/VOLUME):")
            if p_q == "LINE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x= Symbol('x')
                m_n=input("ENTER THE FUNCTION:")
                print(integrate(m_n, x))
            elif p_q == "SURFACE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x,y=symbols('x y')
                m_n=input("ENTER THE FUNCTION:")
                print(integrate(m_n, x, y))
                
            elif p_q == "VOLUME":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x,y,z=symbols('x y z')
                m_n = input("ENTER THE FUNCTION:")
                print (integrate(m_n, x, y, z))
            else:
                 print("INVALID INPUT")
        elif w == "TRIGONOMETRIC":
            a_y=input("WHICH TYPE FO INTEGRAL DO YOU WANT(SINGLE/DOUBLE/TRIPLE):")
            if a_y == "SINGLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x= Symbol('x')
                m_n=input("ENTER THE FUNCTION:")
                print(integrate(m_n, x))
            elif a_y == "DOUBLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x,y=symbols('x y')
                m_n=input("ENTER THE FUNCTION:")
                print(integrate(m_n, x, y))
            elif a_y == "TRIPLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x,y,z=symbols('x y z')
                m_n = input("ENTER THE FUNCTION:")
                print (integrate(m_n, x, y, z))
            else:
                print("INPUT INVALID")
                
                
                 
        
        elif w == "LOGARITHMIC":
             a_y=input("WHICH TYPE FO INTEGRAL DO YOU WANT(SINGLE/DOUBLE/TRIPLE):")
             if a_y == "SINGLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x= Symbol('x')
                m_n=input("ENTER THE FUNCTION:")
                print(integrate(log(m_n), x))
             elif a_y == "DOUBLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x,y=symbols('x y')
                m_n=input("ENTER THE FUNCTION:")
                print(integrate(log(m_n), x, y))
             elif a_y == "TRIPLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x,y,z=symbols('x y z')
                m_n = input("ENTER THE FUNCTION:")
                print (integrate(log(m_n), x, y, z))
             else:
                print("INVALID INPUT")    
            
            
            
        elif w == "EXPONENTIAL":
            print("USE exp() FOR EULER'S NUMBER")
            a_y=input("WHICH TYPE FO INTEGRAL DO YOU WANT(SINGLE/DOUBLE/TRIPLE):")
            if a_y == "SINGLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x= Symbol('x')
                m_n=input("ENTER THE FUNCTION:")
                print(integrate(exp(m_n), x))
            elif a_y == "DOUBLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x,y=symbols('x y')
                m_n=input("ENTER THE FUNCTION:")
                print(integrate(exp(m_n), x, y))
            elif a_y == "TRIPLE":
                from sympy import *
                init_printing(use_unicode=False, wrap_line=False)
                x,y,z=symbols('x y z')
                m_n = input("ENTER THE FUNCTION:")
                print (integrate(exp(m_n), x, y, z))
            else:
                print("INVALID INPUT")    
                
                
            
        else:
            print("PLEASE ENTER VALID INPUT")
    else:
        print("INVALID INPUT")
            
            
                
elif E == "PRIME_IDENTIFICATION":
    D_R = int(input("HOW MANY TIMES YOU WANT TO IDENTIFY PRIMES:"))
    for i in range (D_R):
      a_z = int(input("ENTER THE NUMBER:"))
      if a_z>1:
        for i in range(2,a_z):
            if a_z%i==0:
                print("THE NUMBER IS COMPOSITE")
                break
        else:
            print("THE NUMBER IS PRIME")
      else:
         print("INVALID INPUT")
    i=i+1        

elif E == "2_BY_2_PARTITIONS":
    S_D = int(input("ENTER THE NUMBER:"))
    for i in range (n):
       print(i,"+", n-i)
    i=i+1    
elif E == "COMBINATORIAL_CALCULATIONS":
    q_s = input("WHICH TYPE OF OPERATION DO YOU WANT?(FACTORIAL_CALCULATIONS/COMBINATORICS):")
    if q_s == "FACTORIAL_CALCULATIONS":
        W_E = int(input("ENTER THE NUMBER:"))
        fact = 1
        for a in range(1,W_E+1):
         fact = fact*a
        print(fact)
    elif q_s == "COMBINATORICS":
        a_s = input("DO YOU WANT TO TEST THE RULE OF SUM OR PRODUCT?(TYPE YES/NO):")
        if a_s == "YES":
            q_r = input("WHICH ONE?(SUM OR PRODUCT):")
            if q_r == "SUM":
                A_Q = int(input("WITH HOW MANY SETS DO YOU WNAT TO WORK:"))
                W_E = int(input("")) 
        
         
        
   
                
                
            
            
             
                 
             
            
            
       
elif E == "FUN_ZONE":
    print("WELCOME TO THE FUN ZONE OF PyCalc. HERE YOU CAN DRAW DIFFERENT 3-D AND 2-D SHAPES OF DIFFERENT DIMENAIONS.")
    a_t = input("WHAT DO YOU WANT TO DRAW?(2-D/3-D):")
    if a_t == "2-D":
        a_yo=input("WHICH SHAPE?(SQUARES/RECTANGLES/POLYGONS):")
        if a_yo == "SQUARE":
            a_oy=int(input("ENTER THE SIDE LENGTH:")) 
            import turtle
            pd=turtle.Screen()
            pd=turtle.Turtle()
            for i in range (5):
                pd.forward(a_oy)
                pd.left(90)
        elif a_yo == "RECTANGLE":
            a_oy=int(input("ENTER THE LENGTH:"))
            a_ot=int(input("ENTER THE BREADTH:"))
            import turtle
            pd=turtle.Screen()
            pd=turtle.Turtle()
            pd.forward(a_oy)
            pd.left(90)
            pd.forward(a_ot)
            pd.left(90)
            pd.forward(a_oy)
            pd.left(90)
            pd.forward(a_ot)
        elif a_yo == "POLYGONS":
            tess = int(input("ENTER THE NUMBER OF SIDES OF THE POLYGON:"))
            l_en = int(input("ENTER THE LENGTH OF EACH SIDE:"))
            cd = ((tess-2)*180)/tess
            sa = 180-cd
            import turtle
            fg = turtle.Screen()
            fg = turtle.Turtle()
            for i in range(tess+1):
                fg.forward(l_en)
                fg.left(sa)
        else:
            print("INVALID")
    elif a_t == "3-D":
        a_op = input("WHICH SHAPE?(CUBE/CUBOID)")
        if a_op == "CUBE":
            pid = int(input("ENTER THE SIDE LENGTH:"))
            import turtle
            pd=turtle.Screen()
            pd=turtle.Turtle()
            for i in range (5):
              pd.forward(pid)
              pd.left(90)
              i=i+1
            pd.right(45)
            pd.forward(pid)
            pd.left(45)
            pd.left(90)
            pd.forward(pid)
            pd.left(45)
            pd.forward(pid)
            pd.right(45)
            pd.right(90)
            pd.forward(pid)
            pd.right(45)
            pd.forward(pid)
            pd.right(45)
            pd.forward(pid)
            pd.right(90) 
            pd.right(45)
            pd.forward(pid)
            pd.right(180)
            pd.forward(pid)
            pd.right(135)
            pd.forward(pid)
            pd.right(90)
            pd.forward(pid)
            pd.right(90)
            pd.forward(pid)
        else:
            print("INVALID")
            
    else:
        print("PLESE ENTER CORRECTLY!")
            

 
            
               
               
       
    
L=["ADD-ADD","ADD-SUBSTRACT","ADD-MULTIPLY","ADD-DIVIDE","SUBSTRACT-ADD","SUBSTRACT-SUBSTRACT","SUBSTRACT-MULTIPLY","SUBSTRACT-DIVIDE","MULTIPLY-ADD","MULTIPLY-SUBSTRACT","MULTIPLY-MULTIPLY","MULTIPLY-DIVIDE","DIVIDE-ADD","DIVIDE-SUBSTRACT","DIVIDE-MULTIPLY","DIVIDE-DIVIDE"]    
F=print("DO YOU WANT TO WORK WITH MORE NUMBERS?")
G=input("TYPE YES OR NO:")
if G == "YES":
    H=input("HOW MANY NUMBERS?:")
    if H == "3":
        I=int(input("ENTER THE FIRST NUMBER:"))
        J=int(input("ENTER THE SECOND NUMBER:"))
        K=int(input("ENTER THE THIRD NUMBER:"))
        print("YOU CAN SELECT FROM THE FOLLOWING OPERATIONS and TYPE THEIR RESPECTIVE CODES FOR NUMBERS a,b,c:")
        print(" L(0) : a+b+c ")
        print(" L(1) : a+b-c ")
        print(" L(2) : a+b*c ")
        print(" L(3) : a+b/c ")
        print(" L(4) : a-b+c ")
        print(" L(5) : a-b-c ")
        print(" L(6) : a-b*c ")
        print(" L(7) : a-b/c ")
        print(" L(8) : a*b+c ")
        print(" L(9) : a*b-c ")
        print(" L(10) : a*b*c ")
        print(" L(11) : a*b/c ")
        print(" L(12) : a/b+c ")
        print(" L(13) : a/b-c ")
        print(" L(14) : a/b*c ")
        print(" L(15) : a/b/c ")
        M=input("ENTER THE CODE OF THE OPERATION OF YOUR CHOICE:")
        if M == "L(0)":
            print(I+J+K)
            print(L[0])
            print("THE LIST:")
            print(L)
        elif M == "L(1)":
            print(I+J-K)
            print(L[1])
            print("THE LIST:")
            print(L)
        elif M == "L(2)":
            print(I+J*K)
            print(L[2])
            print("THE LIST:")
            print(L)
        elif M == "L(3)":
            print(I+J/K)
            print(L[3])
            print("THE LIST:")
            print(L)
        elif M == "L(4)":
            print(I-J+K)
            print(L[4])
            print("THE LIST:")
            print(L)
        elif M == "L(5)":
            print(I-J-K)
            print(L[5])
            print("THE LIST:")
            print(L)
        elif M == "L(6)":
            print(I-J*K)
            print(L[6])
            print("THE LIST:")
            print(L)
        elif M == "L(7)":
            print(I-J/K)
            print(L[7])
            print("THE LIST:")
            print(L)
        elif M == "L(8)":
            print(I*J+K)
            print(L[8])
            print("THE LIST:")
            print(L)
        elif M == "L(9)":
            print(I*J-K)
            print(L[9])
            print("THE LIST:")
            print(L)
        elif M == "L(10)":
            print(I*J*K)
            print(L[10])
            print("THE LIST:")
            print(L)
        elif M == "L(11)":
            print(I*J/K)
            print(L[11])
            print("THE LIST:")
            print(L)
        elif M == "L(12)":
            print(I/J+K)
            print(L[12])
            print("THE LIST:")
            print(L)
        elif M == "L(13)":
            print(I/J-K)
            print(L[13])
            print("THE LIST:")
            print(L)
        elif M == "L(14)":
            print(I/J*K)
            print(L[14])
            print("THE LIST:")
            print(L)
        elif M == "L(15)":
            print(I/J/K)
            print(L[15])
            print("THE LIST:")
            print(L)
        else:
            print("CODE IS INCORRECT")
    elif H == "4":
         N=("ADD-ADD-ADD","ADD-ADD-SUBSTRACT","ADD-ADD-MULTIPLY","ADD-ADD-DIVISION","ADD-SUBSTRACT-ADD","ADD-SUBSTRACT-SUBSTRACT","ADD-SUBSTRACT-MULTIPLY","ADD-SUBSTRACT-DIVIDE","ADD-MULTIPLY-ADD","ADD-MULTIPLY-SUBSTRACT","ADD-MULTIPLY-MULTIPLY","ADD-MULTIPLY-DIVIDE","ADD-DIVIDE-ADD","ADD-DIVIDE-SUBSTRACT","ADD-DIVIDE-MULTIPLY","ADD-DIVIDE-DIVIDE","SUBSTRACT-ADD-ADD","SUBSTRACT-ADD-SUBSTRACT","SUBSTRACT-ADD-MULTIPLY","SUBSTRACT-ADD-DIVIDE","SUBSTRACT-SUBSTRACT-ADD","SUBSTRACT-SUBSTRACT-SUBSTRACT","SUBSTRACT-SUBSTRACT-MULTIPLY","SUBSTRACT-SUBSTRACT-DIVIDE","SUBSTRACT-MULTIPLY-ADD","SUBSTRACT-MULTIPLY-SUBSTRACT","SUBSTRACT-MULTIPLY-MULTIPLY","SUBSTRACT-MULTIPLY-DIVIDE","SUBSTRACT-DIVIDE-ADD","SUBSTRACT-DIVIDE-SUBSTRACT","SUBSTRACT-DIVIDE-MULTIPLY","SUBSTRACT-DIVIDE-DIVIDE","MULTIPLY-ADD-ADD","MULTIPLY-ADD-SUBSTRACT","MULTIPLY-ADD-MULTIPLY","MULTIPLY-ADD-DIVIDE","MULTIPLY-SUBSTRACT-ADD","MULTIPLY-SUBSTRACT-SUBSTRACT","MULTIPLY-SUBSTRACT-MULTIPLY","MULTIPLY-SUBSTRACT-DIVISION","MULTIPLY-MULTIPLY-ADD","MULTIPLY-MULTIPLY-SUBSTRACT","MULTIPLY-MULTIPLY-MULTIPLY","MULTIPLY-MULTIPLTY-DIVISION","MULTIPLY-DIVIDE-ADD","MULTIPLY-DIVIDE-SUBSTRACT","MULTIPLY-DIVIDE-MULTIPLY","MULTIPLY-DIVIDE-DIVIDE","DIVIDE-ADD-ADD","DIVIDE-ADD-SUBSTRACT","DIVIDE-ADD-MULTIPLY","DIVIDE-ADD-DIVIDE","DIVIDE-SUBSTRACT-ADD","DIVIDE-SUBSTRACT-SUBSTRACT","DIVIDE-SUBSTRACT-MULTIPLY","DIVIDE-SUBSTRACT-DIVIDE","DIVIDE-MULTIPLY-ADD","DIVIDE-MULTIPLY-SUBSTRACT","DIVIDE-MULTIPLY-MULTIPLY","DIVIDE-MULTIPLY-DIVIDE","DIVIDE-DIVIDE-ADD","DIVIDE-DIVIDE-SUBSTRACT","DIVIDE-DIVIDE-MULTIPLY","DIVIDE-DIVIDE-DIVIDE")
         O=int(input("ENTER THE FIRST NUMBER:"))
         P=int(input("ENTER THE SECOND NUMBER:"))
         Q=int(input("ENTER THE THIRD NUMBER:"))
         R=int(input("ENTER THE FOURTH NUMBER:"))
         print("YOU CAN SELECT THE OPERATIONS OF OUR CHOICE FROM BELOW CONSIDERING ANY THREE INTEGERS a,b,c,d :")
         print(" N(0) : a+b+c+d ")
         print(" N(1) : a+b+c-d ")
         print(" N(2) : a+b+c*d ")
         print(" N(3) : a+b+c/d ")
         print(" N(4) : a+b-c+d ")
         print(" N(5) : a+b-c-d ")
         print(" N(6) : a+b-c*d ")
         print(" N(7) : a+b-c/d ")
         print(" N(8) : a+b*c+d ")
         print(" N(9) : a+b*c-d ")
         print(" N(10) : a+b*c*d ")
         print(" N(11) : a+b*c/d ")
         print(" N(12) : a+b/c+d ")
         print(" N(13) : a+b/c-d ")
         print(" N(14) : a+b/c*d ")
         print(" N(15) : a+b/c/d ")
         print(" N(16) : a-b+c+d ")
         print(" N(17) : a-b+c-d ")
         print(" N(18) : a-b+c*d ")
         print(" N(19) : a-b+c/d ")
         print(" N(20) : a-b-c+d ")
         print(" N(21) : a-b-c-d ")
         print(" N(22) : a-b-c*d ")
         print(" N(23) : a-b-c/d ")
         print(" N(24) : a-b*c+d ")
         print(" N(25) : a-b*c-d ")
         print(" N(26) : a-b*c*d ")
         print(" N(27) : a-b*c/d ")
         print(" N(28) : a-b/c+d ")
         print(" N(29) : a-b/c-d ")
         print(" N(30) : a-b/c*d ")
         print(" N(31) : a-b/c/d ")
         print(" N(32) : a*b+c+d ")
         print(" N(33) : a*b+c-d ")
         print(" N(34) : a*b+c*d ")
         print(" N(35) : a*b+c/d ")
         print(" N(36) : a*b-c+d ")
         print(" N(37) : a*b-c-d ")
         print(" N(38) : a*b-c*d ")
         print(" N(39) : a*b-c/d ")
         print(" N(40) : a*b*c+d ")
         print(" N(41) : a*b*c-d ")
         print(" N(42) : a*b*c*d ")
         print(" N(43) : a*b*c/d ")
         print(" N(44) : a*b/c+d ")
         print(" N(45) : a*b/c-d ")
         print(" N(46) : a*b/c*d ")
         print(" N(47) : a*b/c/d ")
         print(" N(48) : a/b+c+d ")
         print(" N(49) : a/b+c-d ")
         print(" N(50) : a/b+c*d ")
         print(" N(51) : a/b+c/d ")
         print(" N(52) : a/b-c+d ")
         print(" N(53) : a/b-c-d ")
         print(" N(54) : a/b-c*d ")
         print(" N(55) : a/b-c/d ")
         print(" N(56) : a/b*c+d ")
         print(" N(57) : a/b*c-d ")
         print(" N(58) : a/b*c*d ")
         print(" N(59) : a/b*c/d ")
         print(" N(60) : a/b/c+d ")
         print(" N(61) : a/b/c-d ")
         print(" N(62) : a/b/c*d ")
         print(" N(63) : a/b/c/d ")
         S=input("ENTER THE CODE OF YOUR CHOICE:")

         if S == "N(0)":
             print(O+P+Q+R)
             print("THE OPERATION:")
             print(N[0])
         elif S == "N(1)":
             print(O+P+Q-R)
             print("THE OPERATION:")
             print(N[1])
         elif S == "N(2)":
             print(O+P+Q*R)
             print("THE OPERATION:")
             print(N[2])
         elif S == "N(3)":
             print(O+P+Q/R)
             print("THE OPERATION:")
             print(N[3])
         elif S == "N(4)":
             print(O+P-Q+R)
             print("THE OPERATION:")
             print(N[4])
         elif S == "N(5)":
             print(O+P-Q-R)
             print("THE OPERATION:")
             print(N[5])
         elif S == "N(6)":
             print(O+P-Q*R)
             print("THE OPERATION:")
             print(N[6])
         elif S == "N(7)":
             print(O+P-Q/R)
             print("THE OPERATION:")
             print(N[7])
         elif S == "N(8)":
             print(O+P*Q+R)
             print("THE OPERATOR:")
             print(N[8])
         elif S == "N(9)":
             print(O+P*Q-R)
             print("THE OPERATOR:")
             print(N[9])
         elif S == "N(10)":
             print(O+P*Q*R)
             print("THE OPERATOR:")
             print(N[10])
         elif S == "N(11)":
             print(O+P*Q/R)
             print("THE OPERATOR:")
             print(N[11])
         elif S == "N(12)":
             print(O+P/Q+R)
             print("THE OPERATOR:")
             print(N[12])
         elif S == "N(13)":
             print(O+P/Q-R)
             print("THE OPERATOR:")
             print(N[13])
         elif S == "N(14)":
             print(O+P/Q*R)
             print(N[14])
         elif S == "N(15)":
             print(O+P/Q/R)
             print(N[15])
         elif S == "N(16)":
             print(O-P+Q+R)
             print("THE OPERATOR:")
             print(N[16])
         elif S == "N(17)":
             print(O-P+Q-R)
             print("THE OPERATOR:")
             print(N[17])
         elif S == "N(18)":
             print(O-P+Q*R)
             print("THE OPERATOR:")
             print(N[18])
         elif S == "N(19)":
             print(O-P+Q/R)
             print("THE OPERATOR:")
             print(N[19])
         elif S == "N(20)":
             print(O-P-Q+R)
             print("THE OPERATOR:")
             print(N[20])
         elif S == "N(21)":
             print(O-P-Q-R)
             print("THE OPERATOR:")
             print(N[21])
         elif S == "N(22)":
             print(O-P-Q*R)
             print("THE OPERATOR:")
             print(N[22])
         elif S == "N(23)":
             print(O-P-Q/R)
             print("THE OPERATOR")
         elif S == "N(24)":
             print(O-P*Q+R)
             print("THE OPERATOR:")
             print(N[24])
         elif S == "N(25)":
             print(O-P*Q-R)
             print("THE OPERATOR:")
             print(N[25])
         elif S == "N(26)":
             print(O-P*Q*R)
             print("THE OPERATOR:")
             print(N[26])
         elif S == "N(27)":
             print(O-P*Q/R)
             print("THE OPERATOR:")
             print(N[27])
         elif S == "N(28)":
             print(O-P/Q+R)
             print("THE OPERATOR:")
             print(N[28])
         elif S == "N(29)":
             print(O-P/Q-R)
             print("THE OPERATOR:")
             print(N[29])
         elif S == "N(30)":
             print(O-P/Q*R)
             print("THE OPERATOR:")
             print(N[30])
         elif S == "N(31)":
             print(O-P/Q/R)
             print("THE OPERATOR:")
             print(N[31])
         elif S == "N(32)":
             print(O*P+Q+R)
             print("THE OPERATOR:")
             print(N[32])
         elif S == "N(33)":
             print(O*P+Q-R)
             print("THE OPERATOR:")
             print(N[33])
         elif S == "N(34)":
             print(O*P+Q*R)
             print("THE OPERATOR:")
             print(N[34])
         elif S == "N(35)":
             print(O*P+Q/R)
             print("THE OPERATOR:")
             print(N[35])
         elif S == "N(36)":
             print(O*P-Q+R)
             print("THE OPERATOR:")
             print(N[36])
         elif S == "N(37)":
             print(O*P-Q-R)
             print("THE OPERATOR:")
             print(N[37])
         elif S == "N(38)":
             print(O*P-Q*R)
             print("THE OPERATOR:")
             print(N[38])
         elif S == "N(39)":
             print(O*P-Q/R)
             print("THE OPERATOR:")
             print(N[39])
         elif S == "N(40)":
             print(O*P*Q+R)
             print("THE OPERATOR:")
             print(N[40])
         elif S == "N(41)":
             print(O*P*Q-R)
             print("THE OPERATOR:")
             print(N[41])
         elif S == "N(42)":
             print(O*P*Q*R)
             print("THE OPERATOR:")
             print(N[42])
         elif S == "N(43)":
             print(O*P*Q/R)
             print("THE OPERATOR:")
             print(N[43])
         elif S == "N(44)":
             print(O*P/Q+R)
             print("THE OPERATOR:")
             print(N[44])
         elif S == "N(45)":
             print(O*P/Q-R)
             print("THE OPERATOR:")
             print(N[45])
         elif S == "N(46)":
             print(O*P/Q*R)
             print("THE OPERATOR:")
             print(N[46])
         elif S == "N(47)":
             print(O*P/Q/R)
             print("THE OPERATOR:")
             print(N[47])
         elif S == "N(48)":
             print(O/P+Q+R)
             print("THE OPERATOR:")
             print(N[48])
         elif S == "N(49)":
             print(O/P+Q-R)
             print("THE OPERATOR:")
             print(N[49])
         elif S == "N(50)":
             print(O/P+Q*R)
             print("THE OPERATOR:")
             print(N[50])
         elif S == "N(51)":
             print(O/P+Q/R)
             print("THE OPERATOR:")
             print(N[51])
         elif S == "N(52)":
             print(O/P-Q+R)
             print("THE OPERATOR:")
             print(N[52])
         elif S == "N(53)":
             print(O/P-Q-R)
             print("THE OPERATOR:")
             print(N[53])
         elif S == "N(54)":
             print(O/P-Q*R)
             print("THE OPERATOR:")
             print(N[54])
         elif S == "N(55)":
             print(O/P-Q/R)
             print("THE OPERATOR:")
             print(N[55])
         elif S == "N(56)":
             print(O/P*Q+R)
             print("THE OPERATOR:")
             print(N[56])
         elif S == "N(57)":
             print(O/P*Q-R)
             print("THE OPERATOR:")
             print(N[57])
         elif S == "N(58)":
             print(O/P*Q*R)
             print("THE OPERATOR:")
             print(N[58])
         elif S == "N(59)":
             print(O/P*Q/R)
             print("THE OPERATOR:")
             print(N[59])
         elif S == "N(60)":
             print(O/P/Q+R)
             print("THE OPERATOR:")
             print(N[60])
         elif S == "N(61)":
             print(O/P/Q-R)
             print("THE OPERATOR:")
             print(N[61])
         elif S == "N(62)":
             print(O/P/Q*R)
             print("THE OPERATOR:")
             print(N[62])
         elif S == "N(63)":
             print(O/P/Q/R)
             print("THE OPERATOR:")
             print(N[63])
         else:
             print("CODE ENTERED IS INCORRECT")
             
    else:
        print("WE DO NOT SUPPORT MORE THAN 4 NUMBERS OR LESS THAN 2 NUMBER")
        import smtplib
        s = input("PLEASE ENTER YOUR NAME:")
        sender_email = "pythoncalc096@gmail.com"
        receiver_email = input("PLEASE ENTER YOUR EMAIL ADDRESS:")
        password = "pycalc2023"
        message = """
        Dear {},
        
        Thank you for using PyCalc. Please share your feedback on pythoncalc096@gmail.com 
        for further developments. We will be adding more operations to it soon. We will 
        keep you updated via email.Please fill up the google form:https://docs.google.com/forms/d/e/1FAIpQLScm-4xrSwI4FbetEitzBF2kd2tQgiNOlEhkfiC_lrVRQ4cVdQ/viewform?usp=sf_link
    
        REGARDS,
        PyCalc
        """.format(s)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("SUCCESSFUL LOGIN")
        server.sendmail(sender_email, receiver_email, message)
        print("CHECK YOUR INBOX")

             
             
             
         
         
                                             
else:
    import smtplib
    s = input("PLEASE ENTER YOUR NAME:")
    sender_email = "pythoncalc096@gmail.com"
    receiver_email = input("PLEASE ENTER YOUR EMAIL ADDRESS:")
    password = "pycalc2023"
    message = """
    Dear {}
    
    Thank you for using PyCalc. Please share your feedback and experience on pythoncalc096@gmail.com 
    for further developments. We will be adding more operations to it soon. We will 
    keep you updated via email.Please fill out the google form:https://docs.google.com/forms/d/e/1FAIpQLScm-4xrSwI4FbetEitzBF2kd2tQgiNOlEhkfiC_lrVRQ4cVdQ/viewform?usp=sf_link
    
    REGARDS,
    PyCalc
    """.format(s)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("SUCCESSFUL LOGIN")
    server.sendmail(sender_email, receiver_email, message)
    print("CHECK YOUR INBOX")

     
 

 







        
              
        
        












