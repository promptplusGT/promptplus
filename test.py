import spacy
nlp = spacy.load('en_core_web_sm')

prompt ="""
#include<iostream>
#include<cmath>
#include<vector>
#include<random>
#include<algorithm>
double n(double v){return 0.5*std::erfc(-v*std::sqrt(0.5));}
double b(bool c,double S,double K,double r,double T,double s){double d1=(log(S/K)+(r+0.5*s*s)*T)/(s*sqrt(T)),d2=d1-s*sqrt(T);return c?S*n(d1)-K*exp(-r*T)*n(d2):K*exp(-r*T)*n(-d2)-S*n(-d1);}
double bi(bool c,int s,double S,double K,double r,double T,double s){double dt=T/s,u=exp(s*sqrt(dt)),d=1/u,p=(exp(r*dt)-d)/(u-d);std::vector<double> p(s+1);for(int i=0;i<=s;i++){p[i]=S*pow(u,s-i)*pow(d,i);double pay=c?std::max(0.0,p[i]-K):std::max(0.0,K-p[i]);p[i]=pay;}for(int j=s-1;j>=0;j--){for(int i=0;i<=j;i++)p[i]=(p[i]*p[i]+(1-p)*p[i+1])*exp(-r*dt);}return p[0];}
double m(bool c,int n,double S,double K,double r,double T,double s){std::random_device rd;std::mt19937 g(rd());std::normal_distribution<> d(0,1);std::vector<double> p;for(int i=0;i<n;++i){double Z=d(g),sp=S*exp((r-0.5*s*s)*T+s*sqrt(T)*Z),pay=c?std::max(sp-K,0.0):std::max(K-sp,0.0);p.push_back(pay);}return exp(-r*T)*std::accumulate(p.begin(),p.end(),0.0)/n;}
int main(){std::cout<<"Hello! I'm your friendly option pricing bot 🤖\n";std::cout<<"Which model would you like to use today? (Type 'Black-Scholes', 'Binomial', or 'Monte Carlo')\n";std::string m,o;std::getline(std::cin,m);std::cout<<"Do you want to price a Call or a Put option? (Type 'Call' or 'Put')\n";std::getline(std::cin,o);bool c=(o=="Call");double S,K,r,T,s;std::cout<<"Enter the current stock price (S): ";std::cin>>S;std::cout<<"Enter the strike price (K): ";std::cin>>K;std::cout<<"Enter the risk-free rate (r) as a decimal (e.g., 0.05 for 5%): ";std::cin>>r;std::cout<<"Enter the time to expiration in years (T): ";std::cin>>T;std::cout<<"Enter the volatility of the stock as a decimal (s): ";std::cin>>s;double p=0.0;if(m=="Black-Scholes"){p=b(c,S,K,r,T,s);std::cout<<"According to the Black-Scholes model, the "<<o<<" option price is: $"<<p<<"\n";}else if(m=="Binomial"){int st;std::cout<<"Enter the number of steps for the binomial model: ";std::cin>>st;p=bi(c,st,S,K,r,T,s);std::cout<<"According to the Binomial model, the "<<o<<" option price is: $"<<p<<"\n";}else if(m=="Monte Carlo"){int sim;std::cout<<"Enter the number of simulations for the Monte Carlo model: ";std::cin>>sim;p=m(c,sim,S,K,r,T,s);std::cout<<"According to the Monte Carlo model, the "<<o<<" option price is: $"<<p<<"\n";}else std::cout<<"Oops! It seems like you entered an unsupported model. Please try again.\n";std::cout<<"Thank you for using the Option Pricing Bot! Have a great day! 😊\n";return 0;}
"""

doc = nlp(prompt)
code_like = any(token.pos_ in {'SYM'} for token in doc)
print(code_like)