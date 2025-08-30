#!/usr/bin/env python3
"""
Create Pre-Sprint 1: Ideation & Documentation Phase Issues
These are the foundational issues that come BEFORE the technical implementation
Focusing on planning, design, documentation, and project setup
"""

import os
import json
import time
import requests
from typing import List, Dict

# GitHub configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set")
    exit(1)

GITHUB_OWNER = 'michael-placeholder'
GITHUB_REPO = 'shadowed-realms'
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_issue(title: str, body: str, labels: List[str]) -> Dict:
    """Create a single GitHub issue"""
    url = f'{GITHUB_API_URL}/issues'
    data = {
        'title': title,
        'body': body,
        'labels': labels
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating issue '{title}': {e}")
        return None

def generate_ideation_documentation_issues():
    """Generate all Pre-Sprint 1 Ideation & Documentation issues"""
    
    issues = []
    
    # PHASE 0: PROJECT IDEATION (Issues -100 to -81)
    ideation_issues = [
        {
            'num': -100,
            'title': 'Brainstorm game concept and core pillars',
            'deliverable': 'concept_document.md with 3 core pillars defined',
            'xp': 100,
            'coins': 50,
            'value': 'Foundation for entire $50,000 project - defines market position'
        },
        {
            'num': -99,
            'title': 'Research Dark Souls-like market and competition',
            'deliverable': 'market_research.pdf with 10+ competitor analysis',
            'xp': 150,
            'coins': 75,
            'value': 'Identifies market gaps worth $10,000+ in differentiation'
        },
        {
            'num': -98,
            'title': 'Define target audience and player personas',
            'deliverable': '3 detailed player_personas.json files',
            'xp': 100,
            'coins': 50,
            'value': 'Targets specific demographics for asset sales ($45,000 market)'
        },
        {
            'num': -97,
            'title': 'Create initial game design document outline',
            'deliverable': 'GDD_outline.md with all sections listed',
            'xp': 75,
            'coins': 40,
            'value': 'Structures development preventing $5,000+ in rework costs'
        },
        {
            'num': -96,
            'title': 'Sketch initial world map and lore concepts',
            'deliverable': 'world_map_v1.png and lore_overview.txt',
            'xp': 200,
            'coins': 100,
            'value': 'Creates IP value for TCG expansion ($15,000 revenue stream)'
        },
        {
            'num': -95,
            'title': 'Define art style and visual direction',
            'deliverable': 'art_bible_v1.pdf with mood boards',
            'xp': 250,
            'coins': 125,
            'value': 'Establishes consistent style for 5000+ assets ($149,000 value)'
        },
        {
            'num': -94,
            'title': 'Create technical requirements document',
            'deliverable': 'tech_requirements.md with platform specs',
            'xp': 100,
            'coins': 50,
            'value': 'Prevents technical debt worth $8,000 in fixes'
        },
        {
            'num': -93,
            'title': 'Establish project timeline and milestones',
            'deliverable': 'project_timeline.gantt exported as PDF',
            'xp': 75,
            'coins': 40,
            'value': 'Ensures on-time delivery of $50,000 project'
        },
        {
            'num': -92,
            'title': 'Define monetization strategy',
            'deliverable': 'monetization_plan.xlsx with revenue projections',
            'xp': 200,
            'coins': 100,
            'value': 'Maps path to $50,000 revenue target with 5 streams'
        },
        {
            'num': -91,
            'title': 'Create risk assessment matrix',
            'deliverable': 'risk_matrix.csv with mitigation strategies',
            'xp': 150,
            'coins': 75,
            'value': 'Prevents $10,000+ in potential losses'
        },
        {
            'num': -90,
            'title': 'Write game narrative outline',
            'deliverable': 'narrative_outline.md with 6 story arcs',
            'xp': 300,
            'coins': 150,
            'value': 'Creates narrative value for game ($197) and TCG ($15,000)'
        },
        {
            'num': -89,
            'title': 'Design core gameplay loop diagram',
            'deliverable': 'gameplay_loop.svg flowchart',
            'xp': 150,
            'coins': 75,
            'value': 'Defines engagement model for player retention'
        },
        {
            'num': -88,
            'title': 'Create character archetype designs',
            'deliverable': '5 character_concepts.png sketches',
            'xp': 200,
            'coins': 100,
            'value': 'Foundation for 200+ character models ($45,000 in assets)'
        },
        {
            'num': -87,
            'title': 'Define combat system mechanics',
            'deliverable': 'combat_mechanics.md with formulas',
            'xp': 250,
            'coins': 125,
            'value': 'Core system affects 300+ animations ($15,000 value)'
        },
        {
            'num': -86,
            'title': 'Plan progression and leveling systems',
            'deliverable': 'progression_system.json with XP tables',
            'xp': 150,
            'coins': 75,
            'value': 'Drives player engagement for course sales ($8,000)'
        },
        {
            'num': -85,
            'title': 'Design UI/UX wireframes',
            'deliverable': 'ui_wireframes.fig (Figma file)',
            'xp': 200,
            'coins': 100,
            'value': 'Templates for 400+ UI assets ($12,000 value)'
        },
        {
            'num': -84,
            'title': 'Create asset production pipeline document',
            'deliverable': 'asset_pipeline.md with workflow diagrams',
            'xp': 175,
            'coins': 85,
            'value': 'Optimizes production of 5000+ assets'
        },
        {
            'num': -83,
            'title': 'Define quality standards checklist',
            'deliverable': 'quality_standards.pdf with criteria',
            'xp': 100,
            'coins': 50,
            'value': 'Ensures marketplace rating 4.5+ stars'
        },
        {
            'num': -82,
            'title': 'Create team structure and roles document',
            'deliverable': 'team_structure.md with RACI matrix',
            'xp': 75,
            'coins': 40,
            'value': 'Efficient resource allocation for $50,000 project'
        },
        {
            'num': -81,
            'title': 'Write project charter and vision statement',
            'deliverable': 'project_charter.pdf signed document',
            'xp': 100,
            'coins': 50,
            'value': 'Aligns all stakeholders on $50,000 goal'
        }
    ]
    
    # PHASE 0.5: COMPREHENSIVE DOCUMENTATION (Issues -80 to -61)
    documentation_issues = [
        {
            'num': -80,
            'title': 'Write complete Game Design Document (GDD)',
            'deliverable': 'GDD_complete.pdf (50+ pages)',
            'xp': 500,
            'coins': 250,
            'value': 'Bible for entire project worth $50,000'
        },
        {
            'num': -79,
            'title': 'Create Technical Design Document (TDD)',
            'deliverable': 'TDD_complete.pdf with architecture diagrams',
            'xp': 400,
            'coins': 200,
            'value': 'Technical blueprint prevents $15,000 in rework'
        },
        {
            'num': -78,
            'title': 'Write Art Bible with style guides',
            'deliverable': 'art_bible_complete.pdf (30+ pages)',
            'xp': 350,
            'coins': 175,
            'value': 'Consistency guide for $149,000 in assets'
        },
        {
            'num': -77,
            'title': 'Create Animation Style Guide',
            'deliverable': 'animation_guide.pdf with reference videos',
            'xp': 300,
            'coins': 150,
            'value': 'Standards for 600+ animations'
        },
        {
            'num': -76,
            'title': 'Document Audio Design specifications',
            'deliverable': 'audio_design.md with frequency charts',
            'xp': 200,
            'coins': 100,
            'value': 'Guide for 300 audio assets ($9,000)'
        },
        {
            'num': -75,
            'title': 'Write Level Design Document',
            'deliverable': 'level_design.pdf with layouts',
            'xp': 350,
            'coins': 175,
            'value': 'Blueprint for environment assets ($30,000)'
        },
        {
            'num': -74,
            'title': 'Create Enemy Design Compendium',
            'deliverable': 'enemy_compendium.pdf with 75 enemies',
            'xp': 400,
            'coins': 200,
            'value': 'Defines combat content worth $20,000'
        },
        {
            'num': -73,
            'title': 'Document Item and Loot Systems',
            'deliverable': 'item_systems.xlsx with drop tables',
            'xp': 250,
            'coins': 125,
            'value': 'Itemization for 350+ items'
        },
        {
            'num': -72,
            'title': 'Write Quest Design Document',
            'deliverable': 'quest_design.md with 50+ quests',
            'xp': 350,
            'coins': 175,
            'value': 'Content structure for game narrative'
        },
        {
            'num': -71,
            'title': 'Create Dialogue Writing Guidelines',
            'deliverable': 'dialogue_guide.pdf with examples',
            'xp': 200,
            'coins': 100,
            'value': 'Standards for NPC interactions'
        },
        {
            'num': -70,
            'title': 'Document Shader Technical Specifications',
            'deliverable': 'shader_specs.md with node graphs',
            'xp': 300,
            'coins': 150,
            'value': 'Technical guide for 200 shaders ($10,000)'
        },
        {
            'num': -69,
            'title': 'Write Networking Architecture Document',
            'deliverable': 'network_architecture.pdf with diagrams',
            'xp': 350,
            'coins': 175,
            'value': 'Multiplayer foundation for future DLC'
        },
        {
            'num': -68,
            'title': 'Create Performance Optimization Guide',
            'deliverable': 'optimization_guide.md with benchmarks',
            'xp': 250,
            'coins': 125,
            'value': 'Ensures 60FPS for positive reviews'
        },
        {
            'num': -67,
            'title': 'Document Save System Architecture',
            'deliverable': 'save_system.pdf with data structures',
            'xp': 200,
            'coins': 100,
            'value': 'Critical system for player retention'
        },
        {
            'num': -66,
            'title': 'Write Localization Guidelines',
            'deliverable': 'localization_guide.xlsx with string IDs',
            'xp': 150,
            'coins': 75,
            'value': 'Enables global market reach'
        },
        {
            'num': -65,
            'title': 'Create Testing Plan Document',
            'deliverable': 'test_plan.pdf with test cases',
            'xp': 200,
            'coins': 100,
            'value': 'Quality assurance for $50,000 project'
        },
        {
            'num': -64,
            'title': 'Document Deployment Strategy',
            'deliverable': 'deployment_strategy.md with CI/CD',
            'xp': 175,
            'coins': 85,
            'value': 'Smooth launch prevents revenue loss'
        },
        {
            'num': -63,
            'title': 'Write Marketing Plan',
            'deliverable': 'marketing_plan.pdf with timeline',
            'xp': 300,
            'coins': 150,
            'value': 'Strategy to reach $50,000 revenue'
        },
        {
            'num': -62,
            'title': 'Create Community Management Guide',
            'deliverable': 'community_guide.md with policies',
            'xp': 150,
            'coins': 75,
            'value': 'Player retention for long-term revenue'
        },
        {
            'num': -61,
            'title': 'Document Post-Launch Content Roadmap',
            'deliverable': 'dlc_roadmap.pdf with 6-month plan',
            'xp': 250,
            'coins': 125,
            'value': 'Path to $100,000+ Year 2 revenue'
        }
    ]
    
    # PHASE 0.7: CONCEPT ART & PROTOTYPES (Issues -60 to -41)
    concept_prototype_issues = [
        {
            'num': -60,
            'title': 'Create hero character concept art',
            'deliverable': 'hero_concepts.psd with 5 variations',
            'xp': 300,
            'coins': 150,
            'value': 'Visual foundation for main character ($5,000 in assets)'
        },
        {
            'num': -59,
            'title': 'Design boss enemy concepts',
            'deliverable': 'boss_concepts.png set of 15 bosses',
            'xp': 400,
            'coins': 200,
            'value': 'Epic encounters drive game sales ($197 per copy)'
        },
        {
            'num': -58,
            'title': 'Sketch environment concept art',
            'deliverable': 'environment_concepts.pdf with 20 locations',
            'xp': 350,
            'coins': 175,
            'value': 'World building for 400+ environment assets'
        },
        {
            'num': -57,
            'title': 'Create weapon design sheets',
            'deliverable': 'weapon_designs.ai with 50 weapons',
            'xp': 250,
            'coins': 125,
            'value': 'Designs for 300 weapon models ($15,000)'
        },
        {
            'num': -56,
            'title': 'Design armor set concepts',
            'deliverable': 'armor_concepts.psd with 25 sets',
            'xp': 300,
            'coins': 150,
            'value': 'Foundation for 250 armor pieces'
        },
        {
            'num': -55,
            'title': 'Create UI mockups in high fidelity',
            'deliverable': 'ui_mockups.fig with all screens',
            'xp': 250,
            'coins': 125,
            'value': 'Professional UI worth $12,000 in assets'
        },
        {
            'num': -54,
            'title': 'Build gameplay prototype in Unity',
            'deliverable': 'prototype_v1.unitypackage',
            'xp': 500,
            'coins': 250,
            'value': 'Proves core mechanics before full development'
        },
        {
            'num': -53,
            'title': 'Create combat system prototype',
            'deliverable': 'combat_prototype.exe build',
            'xp': 400,
            'coins': 200,
            'value': 'Tests core gameplay worth $12,000 development'
        },
        {
            'num': -52,
            'title': 'Build character controller prototype',
            'deliverable': 'character_controller.cs tested script',
            'xp': 300,
            'coins': 150,
            'value': 'Foundation for character system ($8,000)'
        },
        {
            'num': -51,
            'title': 'Prototype inventory system',
            'deliverable': 'inventory_prototype.unitypackage',
            'xp': 250,
            'coins': 125,
            'value': 'Core system for items ($9,000 in content)'
        },
        {
            'num': -50,
            'title': 'Create shader prototypes',
            'deliverable': 'shader_samples.shadergraph (10 shaders)',
            'xp': 350,
            'coins': 175,
            'value': 'Visual style for entire game'
        },
        {
            'num': -49,
            'title': 'Build level greybox prototype',
            'deliverable': 'level_greybox.unity scene file',
            'xp': 200,
            'coins': 100,
            'value': 'Tests level flow and pacing'
        },
        {
            'num': -48,
            'title': 'Create animation test rigs',
            'deliverable': 'test_rigs.fbx with controllers',
            'xp': 300,
            'coins': 150,
            'value': 'Pipeline for 600+ animations'
        },
        {
            'num': -47,
            'title': 'Prototype particle effects',
            'deliverable': 'vfx_prototypes.unitypackage',
            'xp': 250,
            'coins': 125,
            'value': 'Foundation for 500 VFX ($15,000)'
        },
        {
            'num': -46,
            'title': 'Create audio implementation test',
            'deliverable': 'audio_test.unity with FMOD',
            'xp': 200,
            'coins': 100,
            'value': 'Audio system for 300 assets'
        },
        {
            'num': -45,
            'title': 'Build AI behavior prototype',
            'deliverable': 'ai_prototype.cs with state machine',
            'xp': 350,
            'coins': 175,
            'value': 'Enemy AI worth $11,000 in development'
        },
        {
            'num': -44,
            'title': 'Create networking test build',
            'deliverable': 'network_test.exe with 2-player',
            'xp': 400,
            'coins': 200,
            'value': 'Multiplayer foundation for DLC'
        },
        {
            'num': -43,
            'title': 'Prototype save/load system',
            'deliverable': 'save_system.cs with test scene',
            'xp': 250,
            'coins': 125,
            'value': 'Critical feature for player retention'
        },
        {
            'num': -42,
            'title': 'Build performance test scene',
            'deliverable': 'performance_test.unity with metrics',
            'xp': 200,
            'coins': 100,
            'value': 'Optimization baseline for 60FPS'
        },
        {
            'num': -41,
            'title': 'Create vertical slice build',
            'deliverable': 'vertical_slice.exe (15 min gameplay)',
            'xp': 500,
            'coins': 250,
            'value': 'Proof of concept for investors/publishers'
        }
    ]
    
    # PHASE 0.8: TOOLS & PIPELINE SETUP (Issues -40 to -21)
    tools_pipeline_issues = [
        {
            'num': -40,
            'title': 'Set up project management tools',
            'deliverable': 'Screenshot of configured Jira/Trello board',
            'xp': 100,
            'coins': 50,
            'value': 'Project tracking for 10,000 tasks'
        },
        {
            'num': -39,
            'title': 'Configure version control branching strategy',
            'deliverable': 'git_workflow.md with branch diagram',
            'xp': 150,
            'coins': 75,
            'value': 'Prevents merge conflicts costing days'
        },
        {
            'num': -38,
            'title': 'Set up automated build pipeline',
            'deliverable': 'jenkins/github-actions config files',
            'xp': 250,
            'coins': 125,
            'value': 'Saves 100+ hours of manual builds'
        },
        {
            'num': -37,
            'title': 'Create asset naming conventions',
            'deliverable': 'naming_conventions.pdf',
            'xp': 100,
            'coins': 50,
            'value': 'Organization for 5000+ assets'
        },
        {
            'num': -36,
            'title': 'Set up cloud storage for assets',
            'deliverable': 'Screenshot of configured AWS/Google Cloud',
            'xp': 150,
            'coins': 75,
            'value': 'Secure storage for $149,000 in assets'
        },
        {
            'num': -35,
            'title': 'Configure bug tracking system',
            'deliverable': 'bugzilla/mantis setup confirmation',
            'xp': 125,
            'coins': 60,
            'value': 'Quality control for market success'
        },
        {
            'num': -34,
            'title': 'Create automated testing framework',
            'deliverable': 'test_framework.cs with examples',
            'xp': 300,
            'coins': 150,
            'value': 'Prevents bugs that lose sales'
        },
        {
            'num': -33,
            'title': 'Set up documentation wiki',
            'deliverable': 'wiki URL with initial pages',
            'xp': 100,
            'coins': 50,
            'value': 'Knowledge base for team efficiency'
        },
        {
            'num': -32,
            'title': 'Configure code review process',
            'deliverable': 'code_review_checklist.md',
            'xp': 125,
            'coins': 60,
            'value': 'Code quality for 700+ scripts'
        },
        {
            'num': -31,
            'title': 'Set up continuous integration',
            'deliverable': 'CI config with test pipeline',
            'xp': 250,
            'coins': 125,
            'value': 'Automated quality assurance'
        },
        {
            'num': -30,
            'title': 'Create asset validation tools',
            'deliverable': 'asset_validator.py script',
            'xp': 200,
            'coins': 100,
            'value': 'Quality control for marketplace assets'
        },
        {
            'num': -29,
            'title': 'Set up performance profiling tools',
            'deliverable': 'profiler setup guide.pdf',
            'xp': 150,
            'coins': 75,
            'value': 'Optimization for positive reviews'
        },
        {
            'num': -28,
            'title': 'Configure analytics tracking',
            'deliverable': 'analytics dashboard screenshot',
            'xp': 175,
            'coins': 85,
            'value': 'Data-driven development decisions'
        },
        {
            'num': -27,
            'title': 'Set up crash reporting system',
            'deliverable': 'crashlytics integration proof',
            'xp': 150,
            'coins': 75,
            'value': 'Fast fixes maintain reputation'
        },
        {
            'num': -26,
            'title': 'Create build automation scripts',
            'deliverable': 'build_scripts.sh tested and working',
            'xp': 200,
            'coins': 100,
            'value': 'One-click builds save hours daily'
        },
        {
            'num': -25,
            'title': 'Set up localization pipeline',
            'deliverable': 'localization tools configured',
            'xp': 175,
            'coins': 85,
            'value': 'Global market accessibility'
        },
        {
            'num': -24,
            'title': 'Configure asset optimization pipeline',
            'deliverable': 'optimization_pipeline.md with tools',
            'xp': 200,
            'coins': 100,
            'value': 'Optimized assets for better performance'
        },
        {
            'num': -23,
            'title': 'Set up backup and recovery system',
            'deliverable': 'backup policy document and proof',
            'xp': 150,
            'coins': 75,
            'value': 'Protects $50,000 project investment'
        },
        {
            'num': -22,
            'title': 'Create development environment setup guide',
            'deliverable': 'dev_setup_guide.md step-by-step',
            'xp': 125,
            'coins': 60,
            'value': 'Fast onboarding for team scaling'
        },
        {
            'num': -21,
            'title': 'Configure communication channels',
            'deliverable': 'Screenshot of Discord/Slack setup',
            'xp': 75,
            'coins': 40,
            'value': 'Team coordination for efficiency'
        }
    ]
    
    # PHASE 0.9: BUSINESS & LEGAL (Issues -20 to -1)
    business_legal_issues = [
        {
            'num': -20,
            'title': 'Register business entity',
            'deliverable': 'Business registration certificate PDF',
            'xp': 200,
            'coins': 100,
            'value': 'Legal foundation for $50,000 revenue'
        },
        {
            'num': -19,
            'title': 'Set up business bank account',
            'deliverable': 'Account confirmation (redacted)',
            'xp': 100,
            'coins': 50,
            'value': 'Financial infrastructure for revenue'
        },
        {
            'num': -18,
            'title': 'Create asset license agreements',
            'deliverable': 'license_agreement.pdf template',
            'xp': 250,
            'coins': 125,
            'value': 'Legal protection for $149,000 in assets'
        },
        {
            'num': -17,
            'title': 'Register trademarks',
            'deliverable': 'Trademark application proof',
            'xp': 300,
            'coins': 150,
            'value': 'IP protection for brand value'
        },
        {
            'num': -16,
            'title': 'Create privacy policy',
            'deliverable': 'privacy_policy.html',
            'xp': 150,
            'coins': 75,
            'value': 'Legal compliance for data collection'
        },
        {
            'num': -15,
            'title': 'Write terms of service',
            'deliverable': 'terms_of_service.html',
            'xp': 150,
            'coins': 75,
            'value': 'User agreement for service protection'
        },
        {
            'num': -14,
            'title': 'Set up payment processing',
            'deliverable': 'Payment gateway integration proof',
            'xp': 200,
            'coins': 100,
            'value': 'Infrastructure for $50,000 revenue'
        },
        {
            'num': -13,
            'title': 'Create contributor agreements',
            'deliverable': 'contributor_agreement.pdf',
            'xp': 175,
            'coins': 85,
            'value': 'Legal clarity for team contributions'
        },
        {
            'num': -12,
            'title': 'Register for app store accounts',
            'deliverable': 'Developer account confirmations',
            'xp': 125,
            'coins': 60,
            'value': 'Distribution channels for game'
        },
        {
            'num': -11,
            'title': 'Set up marketplace seller accounts',
            'deliverable': 'Unity/Unreal seller account proof',
            'xp': 150,
            'coins': 75,
            'value': 'Sales channel for $149,000 in assets'
        },
        {
            'num': -10,
            'title': 'Create EULA document',
            'deliverable': 'EULA.pdf for game',
            'xp': 175,
            'coins': 85,
            'value': 'End user agreement protection'
        },
        {
            'num': -9,
            'title': 'Set up tax compliance',
            'deliverable': 'Tax registration documents',
            'xp': 200,
            'coins': 100,
            'value': 'Legal compliance for revenue'
        },
        {
            'num': -8,
            'title': 'Create refund policy',
            'deliverable': 'refund_policy.html',
            'xp': 100,
            'coins': 50,
            'value': 'Customer service standards'
        },
        {
            'num': -7,
            'title': 'Set up customer support system',
            'deliverable': 'Support ticket system screenshot',
            'xp': 150,
            'coins': 75,
            'value': 'Customer retention for repeat sales'
        },
        {
            'num': -6,
            'title': 'Create press kit',
            'deliverable': 'press_kit.zip with assets',
            'xp': 200,
            'coins': 100,
            'value': 'Marketing materials for launch'
        },
        {
            'num': -5,
            'title': 'Set up social media accounts',
            'deliverable': 'Links to all social profiles',
            'xp': 75,
            'coins': 40,
            'value': 'Marketing channels for awareness'
        },
        {
            'num': -4,
            'title': 'Create landing page',
            'deliverable': 'Live website URL',
            'xp': 250,
            'coins': 125,
            'value': 'Sales funnel for conversions'
        },
        {
            'num': -3,
            'title': 'Set up email marketing',
            'deliverable': 'Email campaign dashboard screenshot',
            'xp': 150,
            'coins': 75,
            'value': 'Direct marketing for sales'
        },
        {
            'num': -2,
            'title': 'Create investor pitch deck',
            'deliverable': 'pitch_deck.pdf (20 slides)',
            'xp': 400,
            'coins': 200,
            'value': 'Funding for scaling beyond $50,000'
        },
        {
            'num': -1,
            'title': 'Final pre-production review and approval',
            'deliverable': 'preproduction_complete.pdf signed',
            'xp': 500,
            'coins': 250,
            'value': 'Green light for $50,000 production'
        }
    ]
    
    # Combine all issue categories
    all_issues = ideation_issues + documentation_issues + concept_prototype_issues + tools_pipeline_issues + business_legal_issues
    
    return all_issues

def main():
    """Main function to create ideation and documentation issues"""
    print("=" * 60)
    print("SHADOWED REALMS - Pre-Sprint 1: Ideation & Documentation")
    print("Creating 100 foundational issues (ISSUE-(-100) to ISSUE-(-1))")
    print("=" * 60)
    
    issues_to_create = generate_ideation_documentation_issues()
    total_issues = len(issues_to_create)
    
    print(f"\nCreating {total_issues} ideation and documentation issues")
    print("These are the foundation that comes BEFORE Sprint 1")
    
    created_count = 0
    failed_count = 0
    
    for i, issue_data in enumerate(issues_to_create, 1):
        issue_num = issue_data['num']
        title = f"[ISSUE-{issue_num:04d}] {issue_data['title']}"
        
        # Determine which phase this belongs to
        if issue_num >= -100 and issue_num <= -81:
            phase = "Phase 0: Project Ideation"
            epic = "EPIC-000: Ideation & Planning"
        elif issue_num >= -80 and issue_num <= -61:
            phase = "Phase 0.5: Comprehensive Documentation"
            epic = "EPIC-000: Ideation & Planning"
        elif issue_num >= -60 and issue_num <= -41:
            phase = "Phase 0.7: Concept Art & Prototypes"
            epic = "EPIC-000: Ideation & Planning"
        elif issue_num >= -40 and issue_num <= -21:
            phase = "Phase 0.8: Tools & Pipeline Setup"
            epic = "EPIC-000: Ideation & Planning"
        else:
            phase = "Phase 0.9: Business & Legal"
            epic = "EPIC-000: Ideation & Planning"
        
        body = f"""## 🎯 {phase}
**Epic**: {epic}
**Sprint**: Pre-Sprint 1 - Ideation & Documentation

## 📦 Deliverable Requirements
**What you must upload:**
- {issue_data['deliverable']}

## 💰 Monetary Value Explanation
**Coin Value**: {issue_data['coins']} coins = ${issue_data['coins'] * 10} project value

**Why this value:**
{issue_data['value']}

## 🎮 XP Justification
**XP Value**: {issue_data['xp']} XP

**Why this XP:**
This foundational work requires strategic thinking and planning skills that will shape the entire project. 
It's essential groundwork that enables all future development.

## ✅ Acceptance Criteria
- [ ] Deliverable created and uploaded
- [ ] Meets quality standards
- [ ] Reviewed and approved
- [ ] Integrated into project documentation

## 🔗 Dependencies
- This issue blocks all Sprint 1 technical implementation
- Foundation for {total_issues - abs(issue_num)} subsequent tasks

## 📊 Impact Metrics
- Contributes to Pre-Production Milestone
- Enables Sprint 1 to begin with clear direction
- Reduces project risk by {10 + (abs(issue_num) % 20)}%

---
*Part of Shadowed Realms RPG - Pre-Production Phase*
*Building the foundation for $50,000+ in revenue*
"""
        
        labels = [
            'issue',
            'pre-sprint-1',
            'ideation-documentation',
            f"xp-{issue_data['xp']}",
            f"coins-{issue_data['coins']}",
            'foundational'
        ]
        
        print(f"\n[{i}/{total_issues}] Creating: {title}")
        print(f"  Phase: {phase}")
        print(f"  XP: {issue_data['xp']}, Coins: {issue_data['coins']}")
        print(f"  Deliverable: {issue_data['deliverable']}")
        
        result = create_issue(title, body, labels)
        
        if result:
            created_count += 1
            print(f"  ✓ Created successfully (#{result['number']})")
        else:
            failed_count += 1
            print(f"  ✗ Failed to create")
        
        # Rate limiting
        if i % 3 == 0:
            print(f"  Pausing for rate limiting...")
            time.sleep(2)
    
    print("\n" + "=" * 60)
    print("IDEATION & DOCUMENTATION PHASE COMPLETE")
    print(f"Successfully created: {created_count} issues")
    print(f"Failed: {failed_count} issues")
    print("=" * 60)
    
    # Calculate totals
    total_xp = sum(issue['xp'] for issue in issues_to_create)
    total_coins = sum(issue['coins'] for issue in issues_to_create)
    total_value = total_coins * 10
    
    print(f"\nPre-Sprint 1 Totals:")
    print(f"Total XP Pool: {total_xp:,}")
    print(f"Total Coins: {total_coins:,}")
    print(f"Total Financial Value: ${total_value:,}")
    print(f"\nThese foundational issues set up the entire project")
    print(f"They must be completed before Sprint 1 technical work begins")
    
    print(f"\nView issues at: https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/issues")

if __name__ == "__main__":
    main()