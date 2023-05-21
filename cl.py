# -*- coding: utf-8 -*-
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def contrastive_loss(temp, embedding, label):
    """
    有监督对比损失
    @param    temp: 温度常数
    @param    embedding: 词向量嵌入
    @param    label: 标签
    """
    # 计算相似度
    cosine_sim = cosine_similarity(embedding, embedding)
    # 从矩阵中删除对角线元素
    dis = cosine_sim[~np.eye(cosine_sim.shape[0], dtype=bool)].reshape(cosine_sim.shape[0], -1)
    # 温度
    dis = dis / temp
    cosine_sim = cosine_sim / temp
    dis = np.exp(dis)
    cosine_sim = np.exp(cosine_sim)

    # 计算行总和
    row_sum = []
    for i in range(len(embedding)):
        row_sum.append(sum(dis[i]))

    contrastive_loss = 0
    # 计算外部的和
    for i in range(len(embedding)):
        n_i = label.tolist().count(label[i]) - 1
        # 每一个样本的损失
        inner_sum = 0
        # 计算内部的和
        for j in range(len(embedding)):
            if label[i] == label[j] and i != j:
                inner_sum = inner_sum + np.log(cosine_sim[i][j] / row_sum[i])
        if n_i != 0:
            # 总的损失
            contrastive_loss += (inner_sum / (-n_i))
        else:
            contrastive_loss += 0
    return contrastive_loss

