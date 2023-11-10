from scipy.constants import Boltzmann
import math 
#玻尔兹曼常数的值
K=Boltzmann
print("玻尔兹曼常数值：",K)
#不变量
#天线的口径
D = 65
#表示天线孔径面积
A =(math.pi*D**2 )/4


#1.系统温度(off-source整个射电接收系统的等效温度，反映了系统的噪声水平)
def Tsys_data( Tcal, Poff,Poffcal):
    """
    :param Tcal:
    :param Poff: 噪声二极管开时频谱仪得到的测量值
    :param Poffcal: 噪声二极管关闭时频谱仪得到的测量值
    """
    return (Tcal*Poff)/(Poffcal-Poff)
#调用函数
Tsys=Tsys_data( 10,2,8)
print(Tsys)


#2.DPFU(射电望远镜感应到央斯基的流量导致的温度升高）
def DPFU_data( eta ):
    return (eta*A)/(2*K)
DPFU=DPFU_data(0.5)
print(DPFU)


#3.SEFD(系统等效流量密度：表示系统噪声对应的流量密度）
def SEFD_data( Tsys,eta):
    """
    :param Tsys:系统温度
    :param A:表示天线孔径面积
    :param eta:天线的效率
    """
    return (2 *K* Tsys)/( eta * A)
 #或者return Tsys/DPFU
#调用函数
SEFD=SEFD_data(3.333,0.5)
print(SEFD)


#4.系统灵敏度(能够检测和测量微弱射电信号的能力)
def Smin_data( T,v, np):
    """
    Smin (系统灵敏度)
    :param T:T表示积分时间
    :param v:表示信号接收带宽
    :param np:表示偏振道道数
    """
    return SEFD/(math.sqrt(v*T*np))
#调用函数
Smin=Smin_data(20,0.5,5)
print(Smin)


#5.天线的增益(表示望远镜接收信号能力的强弱)
def G_data( wave,eta ):
    """
    Gain(增益)
    :param D:表示望远镜的直径
    :param wave:表示波长
    :param eta:表示天线效率
    """
    return ((eta*math.pi**2*D**2)/wave**2)
#调用函数
G=G_data( 7.8,0.5 )
print(G)






