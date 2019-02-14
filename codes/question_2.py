import numpy as np
import math as m
import matplotlib.pyplot as plt
def line_intersect(n1,p1,n2,p2):
    N=np.vstack((n1,n2)).T
    p=np.array([p1,p2])
    return np.matmul(np.linalg.inv(N.T),p.T)
A=np.array([2,3])
B=np.array([4,5])
n_given_line=np.array([-1,4])
p_given_line=-3
n_line_centre_should_pass=A-B
p_line_centre_should_pass=((np.linalg.norm(A))**2-(np.linalg.norm(B))**2)/2
centre=line_intersect(n_given_line,p_given_line,
                      n_line_centre_should_pass,
                      p_line_centre_should_pass)
radius1=np.linalg.norm(centre-A)
radius2=np.linalg.norm(centre-B)
print("centre=",centre)
print("radius=",radius1)
print("radius=",radius2)
theta=np.linspace(0,2*m.pi,100)
lambda1=np.linspace(-2,2,20)
X_line=np.zeros((2,20))
X_ob_line=np.zeros((2,20))
for i in range(20):
    X_line[:,i]=centre+lambda1[i]*np.array([4,-1])
    X_ob_line[:,i]=centre+lambda1[i]*np.array([4,-4])
plt.plot(centre[0]+radius1*np.cos(theta),centre[1]+radius1*np.sin(theta),label='$circle$')
plt.plot(X_line[0,:],X_line[1,:],label='$given\_line$')
plt.plot(X_ob_line[0,:],X_ob_line[1,:],label='$line\_centre\_should\_be\_ on$')

plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1-0.1),A[1]*(1+0.1),"A")
plt.text(B[0]*(1-0.1),B[1]*(1+0.1),'B')
plt.plot(B[0],B[1],'o')
plt.plot(centre[0],centre[1],'o')
plt.text(centre[0]*(1-0.2),centre[1]*(1+0.2),'C')
plt.grid()
plt.legend(loc='best')
plt.show()



    
