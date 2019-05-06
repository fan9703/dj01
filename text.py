
m sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba
#特征抽取
#实例化CountVectorizer
def countvec():
	vector = CountVectorizer()
		#调用fit_transform输入并转换数据

			res = vector.fit_transform(["life is is short ,i like python","life is too too long,i dislike python "])
				#res为稀疏矩阵
					#print(res)
						print(vector.get_feature_names())

							print(res.toarray())

							def dictvec():
								dict = DictVectorizer(sparse=False)#sparse为true时为稀疏矩阵格式

									data = dict.fit_transform([{'city':'北京','temperature':100},{'city':'天津','temperature':70},{'city':'东京','temperature':30}])

										print(dict.get_feature_names())

											print(data)

												return None

												def cutword():
													
														#con1 = jieba.cut_for_search("接着我们继续分析数据有三个数据的数据流的情况")
															con1 = jieba.cut("接着我们继续分析数据有三个数据的数据流的情况")
																con2 = jieba.cut("我们读到了第一个数据，这次我们不能直接返回该数据，因为数据流没有结束")
																	con3 = jieba.cut("因此我们只要保证以相同的概率返回第一个或者第二个数据就可以满足题目要求")

																		c1 = ' '.join(list(con1))
																			c2 = ' '.join(list(con2))
																				c3 = ' '.join(list(con3))

																					return c1,c2,c3

																					def chinesevec():
																						c1,c2,c3 = cutword()
																							print(c1,c2,c3)
																								cv = CountVectorizer()
																									data = cv.fit_transform([c1,c2,c3])
																										print(cv.get_feature_names())
																											print(data.toarray())
																												print(data)

																												if __name__ == '__main__':
																													#dictvec()
																														#countvec()
																															chinesevec()
