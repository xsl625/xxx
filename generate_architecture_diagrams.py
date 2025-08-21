#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI数字人平台架构图生成器
生成11个功能模块的分层架构图
"""

import os
from datetime import datetime

def create_svg_diagram(title, layers, filename, width=1200, height=800):
    """
    创建SVG格式的分层架构图
    """
    # 颜色配置
    colors = {
        'header': '#2E4A62',
        'layer1': '#4A90E2',  # 蓝色系 - 工具层
        'layer2': '#7ED321',  # 绿色系 - 算法层
        'layer3': '#F5A623',  # 橙色系 - 平台层
        'layer4': '#BD10E0',  # 紫色系 - 框架层
        'layer5': '#B8E986',  # 浅绿色 - 数据层
        'layer6': '#50E3C2',  # 青色 - 服务层
        'text': '#FFFFFF',
        'border': '#FFFFFF',
        'background': '#F8F9FA'
    }
    
    # 计算层高度
    layer_height = (height - 120) // len(layers)
    
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            .title-text {{ font-family: 'Microsoft YaHei', Arial, sans-serif; font-size: 24px; font-weight: bold; fill: {colors['header']}; }}
            .layer-title {{ font-family: 'Microsoft YaHei', Arial, sans-serif; font-size: 18px; font-weight: bold; fill: {colors['text']}; }}
            .component-text {{ font-family: 'Microsoft YaHei', Arial, sans-serif; font-size: 14px; fill: {colors['text']}; }}
            .layer-rect {{ stroke: {colors['border']}; stroke-width: 2; rx: 8; ry: 8; }}
            .component-rect {{ stroke: {colors['border']}; stroke-width: 1; rx: 4; ry: 4; }}
        </style>
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <rect width="{width}" height="{height}" fill="{colors['background']}" />
    
    <!-- 标题 -->
    <text x="{width//2}" y="40" text-anchor="middle" class="title-text">{title}</text>
    
'''
    
    # 生成各层
    layer_colors = ['layer1', 'layer2', 'layer3', 'layer4', 'layer5', 'layer6']
    y_offset = 80
    
    for i, layer in enumerate(layers):
        color_key = layer_colors[i % len(layer_colors)]
        layer_y = y_offset + i * layer_height
        
        # 层背景
        svg_content += f'''    <!-- {layer['name']} -->
    <rect x="50" y="{layer_y}" width="{width-100}" height="{layer_height-10}" 
          fill="{colors[color_key]}" class="layer-rect" filter="url(#shadow)" />
    
    <!-- 层标题 -->
    <text x="70" y="{layer_y + 30}" class="layer-title">{layer['name']}</text>
    
'''
        
        # 组件
        if 'components' in layer:
            comp_width = (width - 160) // len(layer['components'])
            comp_height = layer_height - 80
            
            for j, component in enumerate(layer['components']):
                comp_x = 80 + j * comp_width
                comp_y = layer_y + 50
                
                # 组件背景（稍微透明的白色）
                svg_content += f'''    <rect x="{comp_x}" y="{comp_y}" width="{comp_width-10}" height="{comp_height}" 
          fill="rgba(255,255,255,0.2)" class="component-rect" />
    
'''
                
                # 组件文本（支持多行）
                if isinstance(component, list):
                    for k, line in enumerate(component):
                        svg_content += f'''    <text x="{comp_x + comp_width//2 - 5}" y="{comp_y + 25 + k*20}" text-anchor="middle" class="component-text">{line}</text>
'''
                else:
                    svg_content += f'''    <text x="{comp_x + comp_width//2 - 5}" y="{comp_y + comp_height//2}" text-anchor="middle" class="component-text">{component}</text>
'''
        
        # 箭头（除了最后一层）
        if i < len(layers) - 1:
            arrow_y = layer_y + layer_height - 5
            svg_content += f'''    <!-- 箭头 -->
    <polygon points="{width//2-10},{arrow_y} {width//2+10},{arrow_y} {width//2},{arrow_y+15}" 
             fill="{colors['header']}" />
    
'''
    
    svg_content += '</svg>'
    
    # 保存文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"已生成架构图: {filename}")

def generate_all_diagrams():
    """生成所有11个架构图"""
    
    # 24.2.1 模版及基础信息配置功能架构图
    layers_241 = [
        {
            'name': '工具层 (Tools Layer)',
            'components': ['数字人模板设计', '角色配置管理', '场景模板库', '个性化定制', '模板版本控制']
        },
        {
            'name': '算法库层 (Algorithm Library)',
            'components': ['模板匹配算法', '配置验证引擎', '智能推荐', '配置冲突检测', '模板优化算法']
        },
        {
            'name': '开发平台层 (Development Platform)',
            'components': ['模板构建器', '配置管理器', '模板测试', '配置部署', '模板监控']
        },
        {
            'name': '计算框架层 (Computing Framework)',
            'components': ['模板渲染引擎', '配置解析器', '模板缓存', '配置同步', '模板编译']
        },
        {
            'name': '数据层 (Data Layer)',
            'components': ['模板数据库', '配置存储', '用户偏好', '版本历史', '配置备份']
        },
        {
            'name': '通用服务层 (Common Services)',
            'components': ['用户认证', '权限管理', '数据验证', '日志记录', '异常处理']
        }
    ]
    
    create_svg_diagram('24.2.1 模版及基础信息配置功能架构图', layers_241, 
                      '/workspace/diagrams/24.2.1_模版及基础信息配置功能架构图.svg')
    
    # 24.2.2 场景管理功能架构图
    layers_242 = [
        {
            'name': '场景设计层 (Scenario Design Layer)',
            'components': ['场景编辑器', '流程设计器', '规则配置', '场景模板', '场景预览']
        },
        {
            'name': '场景引擎层 (Scenario Engine Layer)',
            'components': ['场景解析引擎', '流程执行引擎', '规则引擎', '状态管理', '事件处理']
        },
        {
            'name': '场景管理层 (Scenario Management Layer)',
            'components': ['场景生命周期', '版本管理', '发布管理', '回滚管理', '场景监控']
        },
        {
            'name': '执行框架层 (Execution Framework Layer)',
            'components': ['任务调度器', '执行容器', '资源管理', '负载均衡', '故障恢复']
        },
        {
            'name': '数据存储层 (Data Storage Layer)',
            'components': ['场景定义库', '执行状态库', '历史记录库', '配置存储', '日志存储']
        },
        {
            'name': '基础服务层 (Foundation Services Layer)',
            'components': ['认证服务', '权限控制', '审计日志', '监控告警', '配置中心']
        }
    ]
    
    create_svg_diagram('24.2.2 场景管理功能架构图', layers_242, 
                      '/workspace/diagrams/24.2.2_场景管理功能架构图.svg')
    
    # 24.2.3 真人驱动及客服常用功能建设架构图
    layers_243 = [
        {
            'name': '交互界面层 (Interaction Interface Layer)',
            'components': ['客服工作台', '真人控制面板', '实时监控界面', '配置管理界面', '数据分析界面']
        },
        {
            'name': '驱动控制层 (Drive Control Layer)',
            'components': ['真人驱动引擎', '动作捕捉系统', '表情控制', '语音同步', '实时渲染']
        },
        {
            'name': '客服业务层 (Customer Service Layer)',
            'components': ['对话管理', '知识库检索', '工单处理', '转人工服务', '质量评估']
        },
        {
            'name': '智能处理层 (AI Processing Layer)',
            'components': ['NLP处理', '意图识别', '情感分析', '智能推荐', '自动回复']
        },
        {
            'name': '数据管理层 (Data Management Layer)',
            'components': ['对话记录', '用户档案', '知识库', '培训数据', '性能数据']
        },
        {
            'name': '基础支撑层 (Infrastructure Support Layer)',
            'components': ['实时通信', '媒体处理', '安全认证', '监控日志', '系统集成']
        }
    ]
    
    create_svg_diagram('24.2.3 真人驱动及客服常用功能建设架构图', layers_243, 
                      '/workspace/diagrams/24.2.3_真人驱动及客服常用功能建设架构图.svg')
    
    # 24.2.4 互动方式与素材配置功能架构图
    layers_244 = [
        {
            'name': '交互设计层 (Interaction Design Layer)',
            'components': ['交互方式设计', '用户体验设计', '界面原型设计', '交互流程设计', '响应式设计']
        },
        {
            'name': '素材管理层 (Material Management Layer)',
            'components': ['素材库管理', '素材分类标签', '版本控制', '素材审核', '素材分发']
        },
        {
            'name': '交互引擎层 (Interaction Engine Layer)',
            'components': ['多模态交互', '手势识别', '语音交互', '文本交互', '视觉交互']
        },
        {
            'name': '内容处理层 (Content Processing Layer)',
            'components': ['素材转码', '格式适配', '质量优化', '内容审核', '智能推荐']
        },
        {
            'name': '存储服务层 (Storage Service Layer)',
            'components': ['素材存储', '元数据管理', '缓存管理', 'CDN分发', '备份恢复']
        },
        {
            'name': '基础设施层 (Infrastructure Layer)',
            'components': ['计算资源', '存储资源', '网络资源', '安全防护', '监控运维']
        }
    ]
    
    create_svg_diagram('24.2.4 互动方式与素材配置功能架构图', layers_244, 
                      '/workspace/diagrams/24.2.4_互动方式与素材配置功能架构图.svg')
    
    # 24.2.5 上线场景与硬件扩展功能架构图
    layers_245 = [
        {
            'name': '场景部署层 (Scenario Deployment Layer)',
            'components': ['场景打包', '环境配置', '自动部署', '版本发布', '回滚机制']
        },
        {
            'name': '硬件适配层 (Hardware Adaptation Layer)',
            'components': ['设备驱动管理', '硬件兼容性', '性能优化', '设备监控', '故障诊断']
        },
        {
            'name': '扩展管理层 (Extension Management Layer)',
            'components': ['插件系统', '扩展接口', '第三方集成', 'API网关', '协议适配']
        },
        {
            'name': '运行时环境层 (Runtime Environment Layer)',
            'components': ['容器编排', '资源调度', '负载均衡', '服务发现', '配置管理']
        },
        {
            'name': '监控运维层 (Monitoring & Operations Layer)',
            'components': ['性能监控', '日志收集', '告警通知', '故障处理', '容量规划']
        },
        {
            'name': '基础资源层 (Infrastructure Resource Layer)',
            'components': ['计算集群', '存储集群', '网络设备', '安全设备', '监控设备']
        }
    ]
    
    create_svg_diagram('24.2.5 上线场景与硬件扩展功能架构图', layers_245, 
                      '/workspace/diagrams/24.2.5_上线场景与硬件扩展功能架构图.svg')
    
    # 24.2.6 服务与营销预测功能架构图
    layers_246 = [
        {
            'name': '业务分析层 (Business Analysis Layer)',
            'components': ['用户行为分析', '营销效果分析', '服务质量分析', '趋势预测', '决策支持']
        },
        {
            'name': '预测模型层 (Prediction Model Layer)',
            'components': ['机器学习模型', '深度学习模型', '统计模型', '时间序列模型', '集成模型']
        },
        {
            'name': '营销引擎层 (Marketing Engine Layer)',
            'components': ['个性化推荐', '精准营销', '活动策划', '用户画像', '转化优化']
        },
        {
            'name': '数据处理层 (Data Processing Layer)',
            'components': ['数据清洗', '特征工程', '数据集成', '实时计算', '批量处理']
        },
        {
            'name': '数据存储层 (Data Storage Layer)',
            'components': ['用户数据', '行为数据', '交易数据', '营销数据', '预测结果']
        },
        {
            'name': '基础服务层 (Foundation Service Layer)',
            'components': ['数据接入', '计算资源', '模型训练', '结果输出', '系统监控']
        }
    ]
    
    create_svg_diagram('24.2.6 服务与营销预测功能架构图', layers_246, 
                      '/workspace/diagrams/24.2.6_服务与营销预测功能架构图.svg')
    
    # 24.2.7 定期策略优化功能架构图
    layers_247 = [
        {
            'name': '策略分析层 (Strategy Analysis Layer)',
            'components': ['策略评估', '效果分析', '问题诊断', '优化建议', '决策支持']
        },
        {
            'name': '优化算法层 (Optimization Algorithm Layer)',
            'components': ['遗传算法', '粒子群算法', '梯度下降', '强化学习', '多目标优化']
        },
        {
            'name': '策略执行层 (Strategy Execution Layer)',
            'components': ['策略配置', '参数调整', '规则更新', '模型重训', '效果验证']
        },
        {
            'name': '监控评估层 (Monitoring & Evaluation Layer)',
            'components': ['性能监控', '效果评估', 'A/B测试', '风险控制', '回滚机制']
        },
        {
            'name': '数据管理层 (Data Management Layer)',
            'components': ['历史数据', '实时数据', '策略参数', '优化结果', '评估指标']
        },
        {
            'name': '调度服务层 (Scheduling Service Layer)',
            'components': ['定时任务', '触发机制', '资源调度', '并发控制', '异常处理']
        }
    ]
    
    create_svg_diagram('24.2.7 定期策略优化功能架构图', layers_247, 
                      '/workspace/diagrams/24.2.7_定期策略优化功能架构图.svg')
    
    # 24.2.8 稳定性提升功能架构图
    layers_248 = [
        {
            'name': '可靠性保障层 (Reliability Assurance Layer)',
            'components': ['故障预防', '容错机制', '降级策略', '熔断保护', '限流控制']
        },
        {
            'name': '监控告警层 (Monitoring & Alerting Layer)',
            'components': ['实时监控', '异常检测', '智能告警', '故障定位', '根因分析']
        },
        {
            'name': '故障处理层 (Fault Handling Layer)',
            'components': ['自动恢复', '故障隔离', '服务切换', '数据恢复', '业务补偿']
        },
        {
            'name': '性能优化层 (Performance Optimization Layer)',
            'components': ['性能调优', '资源优化', '缓存策略', '负载均衡', '并发控制']
        },
        {
            'name': '数据保护层 (Data Protection Layer)',
            'components': ['数据备份', '灾难恢复', '数据一致性', '事务管理', '数据校验']
        },
        {
            'name': '基础设施层 (Infrastructure Layer)',
            'components': ['高可用架构', '分布式部署', '容器化部署', '自动扩缩容', '健康检查']
        }
    ]
    
    create_svg_diagram('24.2.8 稳定性提升功能架构图', layers_248, 
                      '/workspace/diagrams/24.2.8_稳定性提升功能架构图.svg')
    
    # 24.2.9 日志与权限建设功能架构图
    layers_249 = [
        {
            'name': '权限管理层 (Permission Management Layer)',
            'components': ['用户管理', '角色管理', '权限分配', '访问控制', '授权验证']
        },
        {
            'name': '日志采集层 (Log Collection Layer)',
            'components': ['应用日志', '系统日志', '访问日志', '审计日志', '错误日志']
        },
        {
            'name': '安全审计层 (Security Audit Layer)',
            'components': ['操作审计', '权限审计', '数据审计', '合规检查', '风险评估']
        },
        {
            'name': '日志处理层 (Log Processing Layer)',
            'components': ['日志解析', '日志过滤', '日志聚合', '日志分析', '日志告警']
        },
        {
            'name': '存储管理层 (Storage Management Layer)',
            'components': ['日志存储', '权限数据', '审计记录', '索引管理', '数据归档']
        },
        {
            'name': '基础服务层 (Foundation Service Layer)',
            'components': ['身份认证', '单点登录', '加密服务', '证书管理', '安全网关']
        }
    ]
    
    create_svg_diagram('24.2.9 日志与权限建设功能架构图', layers_249, 
                      '/workspace/diagrams/24.2.9_日志与权限建设功能架构图.svg')
    
    # 24.2.10 场景升级功能架构图
    layers_2410 = [
        {
            'name': '升级管理层 (Upgrade Management Layer)',
            'components': ['升级计划', '版本管理', '兼容性检查', '升级策略', '回滚计划']
        },
        {
            'name': '版本控制层 (Version Control Layer)',
            'components': ['版本库管理', '分支管理', '合并策略', '冲突解决', '标签管理']
        },
        {
            'name': '升级执行层 (Upgrade Execution Layer)',
            'components': ['增量升级', '全量升级', '灰度发布', '蓝绿部署', '滚动升级']
        },
        {
            'name': '测试验证层 (Test & Validation Layer)',
            'components': ['自动化测试', '兼容性测试', '性能测试', '回归测试', '验收测试']
        },
        {
            'name': '数据迁移层 (Data Migration Layer)',
            'components': ['数据备份', '结构迁移', '数据转换', '数据验证', '数据恢复']
        },
        {
            'name': '监控运维层 (Monitoring & Operations Layer)',
            'components': ['升级监控', '状态跟踪', '异常处理', '性能监控', '运维支持']
        }
    ]
    
    create_svg_diagram('24.2.10 场景升级功能架构图', layers_2410, 
                      '/workspace/diagrams/24.2.10_场景升级功能架构图.svg')
    
    # 24.2.11 系统建设能力功能架构图
    layers_2411 = [
        {
            'name': '开发工具层 (Development Tools Layer)',
            'components': ['IDE集成', '代码生成', '调试工具', '测试工具', '部署工具']
        },
        {
            'name': '平台服务层 (Platform Service Layer)',
            'components': ['开发平台', '测试平台', '部署平台', '监控平台', '运维平台']
        },
        {
            'name': '框架支撑层 (Framework Support Layer)',
            'components': ['开发框架', '微服务框架', '数据框架', 'AI框架', '前端框架']
        },
        {
            'name': '能力中台层 (Capability Platform Layer)',
            'components': ['通用组件', '业务组件', '算法组件', '数据组件', '安全组件']
        },
        {
            'name': '资源管理层 (Resource Management Layer)',
            'components': ['计算资源', '存储资源', '网络资源', '开发资源', '测试资源']
        },
        {
            'name': '基础设施层 (Infrastructure Layer)',
            'components': ['云原生平台', '容器平台', 'DevOps平台', '数据平台', 'AI平台']
        }
    ]
    
    create_svg_diagram('24.2.11 系统建设能力功能架构图', layers_2411, 
                      '/workspace/diagrams/24.2.11_系统建设能力功能架构图.svg')
    
    print("所有架构图生成完成！")

if __name__ == "__main__":
    # 创建输出目录
    os.makedirs('/workspace/diagrams', exist_ok=True)
    
    # 生成所有架构图
    generate_all_diagrams()