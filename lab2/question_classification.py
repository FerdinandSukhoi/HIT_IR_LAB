'''
使用逻辑斯蒂回归和支持向量机的问题分类
'''


from question_classifier import QuestionClassifier
import json
from strange_json import strange_json_to_array
import config

# 是否验证模型
run_validate = True

# 是否处理测试集
run_predict = False

# 训练集太小，重复三次来防止以下Warning：
# _split.py:680: UserWarning: The least populated class in y has only 1 members, which is less than n_splits=3
train_set_replication=3

classifier = QuestionClassifier(train_set_replication)

if run_validate:
    print('Validating......')
    accuracy = classifier.validate()
    print('Accuracy: ：%.4f%%' % (accuracy * 100))
if run_predict:
    print('Classifying......')
    test_data_set = strange_json_to_array(
        config.test_data_path)
    test_data = [' '.join(item['question']) for item in test_data_set]
    test_label_result = classifier.run(test_data)
    for item, label in zip(test_data_set, test_label_result):
        item['class'] = label
    with open(config.question_classification_result_path, 'w', encoding='utf-8') as f:
        json.dump(f, test_data_set)