<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>猜数字游戏</title>
    <style>
        :root {
            --primary-color: #4b6cb7;
            --secondary-color: #182848;
            --success-color: #2e7d32;
            --warning-color: #ef6c00;
            --error-color: #c62828;
            --bg-color: #f5f7fa;
            --text-color: #333;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            width: 100%;
            max-width: 900px;
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(90deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 25px 30px;
            text-align: center;
        }
        
        h1 {
            font-size: 2.2rem;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        
        .content {
            display: flex;
            flex-wrap: wrap;
        }
        
        .game-section {
            flex: 2;
            min-width: 300px;
            padding: 30px;
            display: flex;
            flex-direction: column;
            gap: 25px;
        }
        
        .customization-section {
            flex: 1;
            min-width: 250px;
            background-color: #f8f9fa;
            padding: 30px;
            border-left: 1px solid #eee;
        }
        
        .game-info {
            display: flex;
            justify-content: space-between;
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        
        .info-item {
            text-align: center;
        }
        
        .info-label {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 5px;
        }
        
        .info-value {
            font-size: 1.4rem;
            font-weight: bold;
            color: var(--primary-color);
        }
        
        .input-section {
            display: flex;
            gap: 10px;
        }
        
        #guessInput {
            flex: 1;
            padding: 15px;
            font-size: 1.1rem;
            border: 2px solid #ddd;
            border-radius: 8px;
            transition: border-color 0.3s;
        }
        
        #guessInput:focus {
            border-color: var(--primary-color);
            outline: none;
        }
        
        .game-btn {
            background: linear-gradient(90deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            border: none;
            padding: 15px 25px;
            font-size: 1.1rem;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        
        .game-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        }
        
        .game-btn:active {
            transform: translateY(1px);
        }
        
        .game-btn:disabled {
            background: #cccccc;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }
        
        .console-section {
            background-color: #1e1e1e;
            color: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            min-height: 300px;
            max-height: 400px;
            overflow-y: auto;
            font-family: 'Courier New', monospace;
            box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
        }
        
        .console-line {
            margin-bottom: 10px;
            line-height: 1.5;
        }
        
        .console-line.user {
            color: #4fc3f7;
        }
        
        .console-line.system {
            color: #f0f0f0;
        }
        
        .console-line.success {
            color: #69f0ae;
            font-weight: bold;
        }
        
        .console-line.error {
            color: #ff5252;
        }
        
        .console-line.warning {
            color: #ffd740;
        }
        
        .history-section {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        
        .history-title {
            font-size: 1.2rem;
            margin-bottom: 15px;
            color: #333;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .history-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .history-item {
            background-color: white;
            padding: 8px 15px;
            border-radius: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            font-weight: bold;
        }
        
        .history-item.correct {
            background-color: #e8f5e9;
            color: var(--success-color);
        }
        
        .history-item.high {
            background-color: #fff3e0;
            color: var(--warning-color);
        }
        
        .history-item.low {
            background-color: #e3f2fd;
            color: var(--primary-color);
        }
        
        .customization-panel {
            margin-bottom: 25px;
        }
        
        .panel-title {
            font-size: 1.3rem;
            margin-bottom: 15px;
            color: #333;
            padding-bottom: 10px;
            border-bottom: 1px solid #ddd;
        }
        
        .form-group {
            margin-bottom: 15px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
            color: #555;
        }
        
        input[type="number"], input[type="text"], select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        
        .color-picker {
            display: flex;
            gap: 10px;
        }
        
        .color-option {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid transparent;
        }
        
        .color-option.active {
            border-color: #333;
        }
        
        footer {
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid #eee;
        }
        
        @media (max-width: 768px) {
            .content {
                flex-direction: column;
            }
            
            .customization-section {
                border-left: none;
                border-top: 1px solid #eee;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>猜数字游戏</h1>
            <p class="subtitle">我已经想了一个1到100之间的数字，请你来猜一猜</p >
        </header>
        
        <div class="content">
            <div class="game-section">
                <div class="game-info">
                    <div class="info-item">
                        <div class="info-label">目标数字</div>
                        <div id="targetNumber" class="info-value">?</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">猜测次数</div>
                        <div id="attemptsCount" class="info-value">0</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">游戏状态</div>
                        <div id="gameStatus" class="info-value">进行中</div>
                    </div>
                </div>
                
                <div class="input-section">
                    <input type="number" id="guessInput" placeholder="请输入你猜的数字（1-100）" min="1" max="100">
                    <button id="submitBtn" class="game-btn">提交猜测</button>
                </div>
                
                <div class="console-section" id="consoleOutput">
                    <div class="console-line system">欢迎来到猜数字游戏！</div>
                    <div class="console-line system">我已经想了一个1到100之间的数字，请你来猜一猜。</div>
                </div>
                
                <div class="history-section">
                    <div class="history-title">
                        <span>猜测历史</span>
                        <button id="resetBtn" class="game-btn">重新开始</button>
                    </div>
                    <div class="history-list" id="historyList">
                        <!-- 猜测历史将在这里显示 -->
                    </div>
                </div>
            </div>
            
            <div class="customization-section">
                <div class="customization-panel">
                    <h2 class="panel-title">游戏设置</h2>
                    
                    <div class="form-group">
                        <label for="rangeMin">最小数字</label>
                        <input type="number" id="rangeMin" value="1" min="1" max="1000">
                    </div>
                    <div class="form-group">
                        <label for="maxAttempts">最大尝试次数</label>
                        <input type="number" id="maxAttempts" value="0" min="0">
                        <small>0表示无限制</small>
                    </div>
                    
                    <button id="applySettings" class="game-btn" style="width: 100%; margin-top: 10px;">应用设置</button>
                </div>
                
                <div class="customization-panel">
                    <h2 class="panel-title">自定义外观</h2>
                    
                    <div class="form-group">
                        <label for="themeSelect">主题</label>
                        <select id="themeSelect">
                            <option value="default">默认主题</option>
                            <option value="dark">暗色主题</option>
                            <option value="nature">自然主题</option>
                            <option value="ocean">海洋主题</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label>主色调</label>
                        <div class="color-picker">
                            <div class="color-option active" style="background-color: #4b6cb7;" data-color="#4b6cb7"></div>
                            <div class="color-option" style="background-color: #e74c3c;" data-color="#e74c3c"></div>
                            <div class="color-option" style="background-color: #2ecc71;" data-color="#2ecc71"></div>
                            <div class="color-option" style="background-color: #9b59b6;" data-color="#9b59b6"></div>
                            <div class="color-option" style="background-color: #f39c12;" data-color="#f39c12"></div>
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label for="titleText">自定义标题</label>
                        <input type="text" id="titleText" value="猜数字游戏" placeholder="输入自定义标题">
                    </div>
                    
                    <button id="applyAppearance" class="game-btn" style="width: 100%; margin-top: 10px;">应用外观</button>
                </div>
            </div>
        </div>
        
        <footer>
            <p>猜数字游戏网页版 | 可自定义设置</p >
        </footer>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // 游戏状态变量
            let secretNumber;
            let attempts;
            let gameActive;
            let minRange = 1;
            let maxRange = 100;
            let maxAttempts = 0;
            
            // DOM元素
            const guessInput = document.getElementById('guessInput');
            const submitBtn = document.getElementById('submitBtn');
            const resetBtn = document.getElementById('resetBtn');
            const consoleOutput = document.getElementById('consoleOutput');
            const historyList = document.getElementById('historyList');
            const targetNumber = document.getElementById('targetNumber');
            const attemptsCount = document.getElementById('attemptsCount');
            const gameStatus = document.getElementById('gameStatus');
            
            // 设置相关元素
            const rangeMinInput = document.getElementById('rangeMin');
            const rangeMaxInput = document.getElementById('rangeMax');
            const maxAttemptsInput = document.getElementById('maxAttempts');
            const applySettingsBtn = document.getElementById('applySettings');
            const themeSelect = document.getElementById('themeSelect');
            const colorOptions = document.querySelectorAll('.color-option');
            const titleTextInput = document.getElementById('titleText');
            const applyAppearanceBtn = document.getElementById('applyAppearance');
            
            // 初始化游戏
            function initGame() {
                secretNumber = Math.floor(Math.random() * (maxRange - minRange + 1)) + minRange;
                attempts = 0;
                gameActive = true;
                
                // 更新UI
                targetNumber.textContent = '?';
                attemptsCount.textContent = '0';
                gameStatus.textContent = '进行中';
                gameStatus.style.color = getComputedStyle(document.documentElement).getPropertyValue('--primary-color');
                
                // 清空控制台和历史记录
                consoleOutput.innerHTML = `
                    <div class="console-line system">欢迎来到猜数字游戏！</div>
                    <div class="console-line system">我已经想了一个${minRange}到${maxRange}之间的数字，请你来猜一猜。</div>
                `;
                historyList.innerHTML = '';
                
                // 启用输入
                guessInput.disabled = false;
                submitBtn.disabled = false;
                guessInput.value = '';
                guessInput.focus();
                
                // 
                // 更新输入框的min和max属性
                guessInput.min = minRange;
                guessInput.max = maxRange;
                guessInput.placeholder = `请输入你猜的数字（${minRange}-${maxRange}）`;
            }
            
            // 添加消息到控制台
            function addConsoleMessage(message, type = 'system') {
                const messageElement = document.createElement('div');
                messageElement.className = `console-line ${type}`;
                messageElement.textContent = message;
                consoleOutput.appendChild(messageElement);
                
                // 自动滚动到底部
                consoleOutput.scrollTop = consoleOutput.scrollHeight;
            }
            
            // 添加猜测到历史记录
            function addToHistory(guess, result) {
                const historyItem = document.createElement('div');
                historyItem.className = `history-item ${result}`;
                historyItem.textContent = guess;
                historyList.appendChild(historyItem);
            }
            
            // 处理猜测
            function processGuess() {
                if (!gameActive) return;
                
                const guess = parseInt(guessInput.value);
                
                // 验证输入
                if (isNaN(guess) || guess < minRange || guess > maxRange) {
                    addConsoleMessage(`请输入有效的数字（${minRange}-${maxRange}）！`, 'error');
                    guessInput.value = '';
                    guessInput.focus();
                    return;
                }
                
                // 增加尝试次数
                attempts++;
                attemptsCount.textContent = attempts;
                
                // 添加用户输入到控制台
                addConsoleMessage(`> ${guess}`, 'user');
                
                // 判断猜测结果
                if (guess < secretNumber) {
                    addConsoleMessage('太小了！再试试看。', 'warning');
                    addToHistory(guess, 'low');
                } else if (guess > secretNumber) {
                    addConsoleMessage('太大了！再试试看。', 'warning');
                    addToHistory(guess, 'high');
                } else {
                    addConsoleMessage(`恭喜你！猜对了！答案是 ${secretNumber}。`, 'success');
                    addConsoleMessage(`你一共猜了 ${attempts} 次。`, 'success');
                    addToHistory(guess, 'correct');
                    
                    // 游戏结束
                    gameActive = false;
                    targetNumber.textContent = secretNumber;
                    gameStatus.textContent = '已获胜';
                    gameStatus.style.color = getComputedStyle(document.documentElement).getPropertyValue('--success-color');
                    
                    // 禁用输入
                    guessInput.disabled = true;
                    submitBtn.disabled = true;
                }
                
            function checkMaxAttempts() {
                if (maxAttempts > 0 && attempts >= maxAttempts && gameActive) {
                    naddConsoleMessage(`很遗憾，你已经用了${maxAttempts}次机会。正确答案是${secretNumber}。`, 'error');
                    gameActive = false;
                    targetNumber.textContent = secretNumber;
                    gameStatus.textContent = '已失败';
                    gameStatus.style.color = getComputedStyle(document.documentElement).getPropertyValue('--error-color');

        // 禁用输入
                    guessInput.disabled = true;
                    submitBtn.disabled = true;
        
                    return true; // 达到最大次数
    }
                    return false; // 未达到最大次数
}

// 在每次猜测后调用这个函数
            function processGuess() {
                 if (!gameActive) return;
    
                     attempts++;
    
    // 检查是否达到最大尝试次数
                 if (checkMaxAttempts()) {
                    return; // 如果达到最大次数，直接返回
    }
    
  
               
                // 清空输入框
                guessInput.value = '';
                guessInput.focus();
            }
            
            // 应用游戏设置
            function applyGameSettings() {
                const newMin = parseInt(rangeMinInput.value);
                const newMax = parseInt(rangeMaxInput.value);
                const newMaxAttempts = parseInt(maxAttemptsInput.value);
                
                // 验证输入
                if (isNaN(newMin) || isNaN(newMax) || newMin >= newMax) {
                    alert('最小数字必须小于最大数字！');
                    return;
                }
                
                if (newMaxAttempts < 0) {
                    alert('最大尝试次数不能为负数！');
                    return;
                }
                
                minRange = newMin;
                maxRange = newMax;
                maxAttempts = newMaxAttempts;
                
                // 重新开始游戏
                initGame();
                
                addConsoleMessage(`游戏设置已更新：范围 ${minRange}-${maxRange}，最大尝试次数 ${maxAttempts === 0 ? '无限制' : maxAttempts}`, 'system');
            }
            
            // 应用外观设置
            function applyAppearanceSettings() {
                const theme = themeSelect.value;
                const titleText = titleTextInput.value || '猜数字游戏';
                
                // 更新标题
                document.querySelector('header h1').textContent = titleText;
                
                // 应用主    
applyTheme(theme);
                
                addConsoleMessage('外观设置已应用！', 'system');
            }
            
            // 应用主题
            function applyTheme(theme) {
                const root = document.documentElement;
                
                switch(theme) {
                    case 'dark':
                        root.style.setProperty('--primary-color', '#2c3e50');
                        root.style.setProperty('--secondary-color', '#1a252f');
                        root.style.setProperty('--bg-color', '#34495e');
                        break;
                    case 'nature':
                        root.style.setProperty('--primary-color', '#27ae60');
                        root.style.setProperty('--secondary-color', '#2ecc71');
                        break;
                    case 'ocean':
                        root.style.setProperty('--primary-color', '#3498db');
                        root.style.setProperty('--secondary-color', '#2980b9');
                        break;
                    default: // default theme
                        root.style.setProperty('--primary-color', '#4b6cb7');
                        root.style.setProperty('--secondary-color', '#182848');
                }
            }
            
            // 事件监听
            submitBtn.addEventListener('click', processGuess);
            
            guessInput.addEventListener('keypress', function(event) {
                if (event.key === 'Enter') {
                    processGuess();
                }
            });
            
            resetBtn.addEventListener('click', initGame);
            
            applySettingsBtn.addEventListener('click', applyGameSettings);
            
            applyAppearanceBtn.addEventListener('click', applyAppearanceSettings);
            
            // 颜色选择器
            colorOptions.forEach(option => {
                option.addEventListener('click', function() {
                    colorOptions.forEach(opt => opt.classList.remove('active'));
                    this.classList.add('active');
                    
                    const color = this.getAttribute('data-color');
                    document.documentElement.style.setProperty('--primary-color', color);
                    
                    // 计算一个较深的颜色作为次要颜色
                    const darkerColor = shadeColor(color, -30);
                    document.documentElement.style.setProperty('--secondary-color', darkerColor);
                });
            });
            
            // 辅助函数：调整颜色深浅
            function shadeColor(color, percent) {
                let R = parseInt(color.substring(1,3),16);
                let G = parseInt(color.substring(3,5),16);
                let B = parseInt(color.substring(5,7),16);

                R = parseInt(R * (100 + percent) / 100);
                G = parseInt(G * (100 + percent) / 100);
                B = parseInt(B * (100 + percent) / 100);

                R = (R<255)?R:255;  
                G = (G<255)?G:255;  
                B = (B<255)?B:255;  

                R = Math.round(R);
                G = Math.round(G);
                B = Math.round(B);

                const RR = ((R.toString(16).length==1)?"0"+R.toString(16):R.toString(16));
                const GG = ((G.toString(16).length==1)?"0"+G.toString(16):G.toString(16));
                const BB = ((B.toString(16).length==1)?"0"+B.toString(16):B.toString(16));

                return "#"+RR+GG+BB;
            }
            
            // 初始化游戏
            initGame();
        });
    </script>
</body>
</html>
```
2.<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>真心话问卷</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', sans-serif; }
        body { background: linear-gradient(135deg, #ffd6e7 0%, #ffb6c1 100%); color: #5a3d5c; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 40px 20px; }
        .container { width: 100%; max-width: 800px; background: rgba(255, 255, 255, 0.9); border-radius: 20px; box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1); overflow: hidden; margin-bottom: 30px; }
        header { background: linear-gradient(to right, #ff8fab, #fb6f92); color: white; padding: 30px 40px; text-align: center; position: relative; }
        header h1 { font-size: 2.5rem; margin-bottom: 10px; font-weight: 700; position: relative; }
        header p { font-size: 1.1rem; opacity: 0.9; position: relative; }
        .form-container { padding: 40px; }
        .form-group { margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px dashed #ffb6c1; }
        label { display: block; margin-bottom: 12px; font-weight: 600; color: #5a3d5c; font-size: 1.1rem; }
        .question-number { display: inline-block; width: 28px; height: 28px; background: #ff8fab; color: white; border-radius: 50%; text-align: center; line-height: 28px; margin-right: 10px; font-size: 0.9rem; }
        input, textarea { width: 100%; padding: 15px 20px; border: 2px solid #f0d2dc; border-radius: 12px; font-size: 1rem; transition: all 0.3s ease; background: #fff9fb; color: #5a3d5c; }
        textarea { min-height: 100px; resize: vertical; }
        input:focus, textarea:focus { border-color: #ff8fab; box-shadow: 0 0 0 3px rgba(255, 143, 171, 0.2); outline: none; background: white; }
        .radio-group { display: flex; flex-wrap: wrap; gap: 15px; margin-top: 10px; }
        .radio-option { display: flex; align-items: center; gap: 8px; }
        .radio-option input { width: auto; }
        .btn-submit { background: linear-gradient(to right, #ff8fab, #fb6f92); color: white; border: none; padding: 16px 30px; font-size: 1.1rem; border-radius: 12px; cursor: pointer; transition: all 0.3s ease; font-weight: 600; width: 100%; margin-top: 20px; box-shadow: 0 5px 15px rgba(255, 143, 171, 0.4); display: flex; align-items: center; justify-content: center; gap: 10px; }
        .btn-submit:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(255, 143, 171, 0.6); }
        .btn-submit:disabled { background: #cccccc; cursor: not-allowed; transform: none; box-shadow: none; }
        .anonymous-note { background: #fff0f5; border-radius: 12px; padding: 20px; margin-top: 30px; text-align: center; border: 1px dashed #ffb6c1; }
        .real-name-option { display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 15px; }
        .real-name-option input { width: auto; }
        .real-name-field { margin-top: 15px; display: none; }
        .footer { color: #5a3d5c; text-align: center; margin-top: 20px; font-size: 0.9rem; opacity: 0.8; }
        .notification { position: fixed; top: 20px; right: 20px; background: #8ce0b8; color: white; padding: 15px 25px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); display: flex; align-items: center; gap: 10px; z-index: 1000; transform: translateX(150%); transition: transform 0.5s ease; }
        .notification.error { background: #fb6f92; }
        .notification.show { transform: translateX(0); }
        .video-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.95); display: none; justify-content: center; align-items: center; z-index: 9999; flex-direction: column; }
        .video-container.active { display: flex; }
        .video-player { width: 100%; height: 100%; object-fit: cover; }
        .video-info { position: absolute; top: 40px; color: white; text-align: center; max-width: 600px; padding: 0 20px; z-index: 10; }
        .video-title { font-size: 2rem; margin-bottom: 10px; color: #ff8fab; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
        .video-description { font-size: 1.2rem; line-height: 1.5; opacity: 0.9; text-shadow: 1px 1px 2px rgba(0,0,0,0.5); }
        .video-warning { position: absolute; bottom: 30px; color: rgba(255, 255, 255, 0.7); font-size: 1rem; text-align: center; width: 100%; padding: 0 20px; z-index: 10; }
        .video-progress { position: absolute; bottom: 80px; width: 90%; max-width: 800px; height: 6px; background: rgba(255, 255, 255, 0.2); border-radius: 3px; overflow: hidden; z-index: 10; }
        .video-progress-bar { height: 100%; background: #ff8fab; width: 0%; transition: width 0.3s ease; }
        .video-loading { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-size: 1.5rem; text-align: center; z-index: 10; display: none; }
        .video-loading.active { display: block; }
        .video-controls { position: absolute; bottom: 100px; display: flex; gap: 15px; z-index: 10; opacity: 0; transition: opacity 0.3s ease; }
        .video-container.active .video-controls { opacity: 1; }
        .video-control-btn { background: rgba(255, 255, 255, 0.2); border: none; color: white; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-size: 1rem; display: flex; align-items: center; gap: 8px; transition: all 0.3s ease; }
        .video-control-btn:hover { background: rgba(255, 255, 255, 0.3); transform: translateY(-2px); }
        .preload-indicator { position: fixed; bottom: 20px; left: 20px; background: rgba(0, 0, 0, 0.7); color: white; padding: 10px 15px; border-radius: 8px; font-size: 0.9rem; z-index: 100; display: none; }
        .preload-indicator.active { display: block; }
        
        /* 游戏继续弹窗样式 */
        .game-continue-modal { 
            position: fixed; 
            top: 0; 
            left: 0; 
            width: 100%; 
            height: 100%; 
            background: rgba(0, 0, 0, 0.8); 
            display: none; 
            justify-content: center; 
            align-items: center; 
            z-index: 10000; 
            flex-direction: column; 
        }
        .game-continue-modal.active { display: flex; }
        .game-continue-content { 
            background: white; 
            border-radius: 20px; 
            padding: 40px; 
            text-align: center; 
            max-width: 500px; 
            width: 90%; 
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3); 
        }
        .game-continue-title { 
            font-size: 2rem; 
            margin-bottom: 15px; 
            color: #ff8fab; 
        }
        .game-continue-description { 
            font-size: 1.1rem; 
            margin-bottom: 25px; 
            color: #5a3d5c; 
            line-height: 1.5; 
        }
        .game-continue-btn { 
            background: linear-gradient(to right, #ff8fab, #fb6f92); 
            color: white; 
            border: none; 
            padding: 15px 30px; 
            font-size: 1.2rem; 
            border-radius: 12px; 
            cursor: pointer; 
            transition: all 0.3s ease; 
            font-weight: 600; 
            box-shadow: 0 5px 15px rgba(255, 143, 171, 0.4); 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            gap: 10px; 
            margin: 0 auto; 
        }
        .game-continue-btn:hover { 
            transform: translateY(-3px); 
            box-shadow: 0 8px 20px rgba(255, 143, 171, 0.6); 
        }
        
        .heart { color: #fb6f92; animation: heartbeat 1.5s ease infinite; }
        @keyframes heartbeat { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }
        @media (max-width: 600px) {
            .container { border-radius: 15px; }
            header { padding: 20px; }
            header h1 { font-size: 1.8rem; }
            .form-container { padding: 25px; }
            .notification { right: 10px; left: 10px; transform: translateY(-150%); }
            .notification.show { transform: translateY(0); }
            .video-title { font-size: 1.5rem; }
            .video-description { font-size: 1rem; }
            .preload-indicator { bottom: 10px; left: 10px; font-size: 0.8rem; padding: 8px 12px; }
            .video-controls { bottom: 70px; flex-direction: column; }
            .video-control-btn { padding: 8px 15px; font-size: 0.9rem; }
            .game-continue-content { padding: 25px; }
            .game-continue-title { font-size: 1.5rem; }
            .game-continue-description { font-size: 1rem; }
        }
    </style>
</head>
<body>
    <div class="preload-indicator" id="preloadIndicator"><i class="fas fa-sync-alt fa-spin"></i> 视频预加载中...</div>
    
    <div class="container">
        <header>
            <h1><i class="fas fa-heart heart"></i> 真心话</h1>
            <p>分享你的想法，让我们更了解彼此（班级内部游戏，请不要外传）</p>
        </header>
        
        <div class="form-container">
            <form id="surveyForm">
                <!-- 性别选择 -->
                <div class="form-group">
                    <label for="gender"><span class="question-number">1</span>你的性别是？</label>
                    <div class="radio-group">
                        <div class="radio-option"><input type="radio" id="male" name="gender" value="男" required><label for="male">男</label></div>
                        <div class="radio-option"><input type="radio" id="female" name="gender" value="女" required><label for="female">女</label></div>
                        <div class="radio-option"><input type="radio" id="secret" name="gender" value="保密" required><label for="secret">保密</label></div>
                    </div>
                </div>
                
                <!-- 问卷问题 - 合理化后的内容 -->
                <div class="form-group">
                    <label for="handsome"><span class="question-number">2</span>你认为我们班级里哪位男生最帅？</label>
                    <input type="text" id="handsome" name="handsome" placeholder="请输入名字（如果觉得没有，可以填写'无'）" required>
                </div>
                
                <div class="form-group">
                    <label for="beautiful"><span class="question-number">3</span>你认为我们班级里哪位女生最漂亮？</label>
                    <input type="text" id="beautiful" name="beautiful" placeholder="请输入名字" required>
                </div>
                
                <div class="form-group">
                    <label for="crush"><span class="question-number">4</span>你最喜欢的游戏是什么？</label>
                    <input type="text" id="crush" name="crush" placeholder="请输入你最喜欢的游戏名称" required>
                </div>
                
                <div class="form-group">
                    <label for="romantic"><span class="question-number">5</span>请分享你在"到梦空间"获得的学分数量</label>
                    <textarea id="romantic" name="romantic" placeholder="请写下你的学分数量，让我们羡慕一下..." required></textarea>
                </div>
                
                <div class="form-group">
                    <label for="crazy"><span class="question-number">6</span>你最喜欢的美食是什么？</label>
                    <textarea id="crazy" name="crazy" placeholder="请描述你最喜欢的美食..." required></textarea>
                </div>
                
                <div class="form-group">
                    <label for="fantasy"><span class="question-number">7</span>你想吃饼干吗？如果想吃，请留下你的名字</label>
                    <textarea id="fantasy" name="fantasy" placeholder="请告诉我们你是否想吃饼干，如果想的话请留下你的名字..." required></textarea>
                </div>
                
                <div class="form-group">
                    <label for="feeling"><span class="question-number">8</span>你现在有什么感受？</label>
                    <textarea id="feeling" name="feeling" placeholder="请描述你现在的感受..." required></textarea>
                </div>
                
                <!-- 匿名选项 -->
                <div class="anonymous-note">
                    <h3><i class="fas fa-user-secret"></i> 匿名填写</h3>
                    <p>本问卷默认匿名填写，你的个人信息不会被公开。</p>
                    <div class="real-name-option"><input type="checkbox" id="real_name_option"><label for="real_name_option">我想实名填写</label></div>
                    <div class="real-name-field" id="real_name_field"><input type="text" id="real_name" name="real_name" placeholder="请输入你的姓名"></div>
                </div>
                
                <button type="submit" class="btn-submit" id="submitBtn"><i class="fas fa-paper-plane"></i> 提交问卷</button>
            </form>
        </div>
    </div>
    
    <!-- 视频播放器 -->
    <div class="video-container" id="videoContainer">
        <div class="video-loading" id="videoLoading"><i class="fas fa-spinner fa-spin"></i> 视频加载中，请稍候...</div>
        <video class="video-player" id="videoPlayer" autoplay muted playsinline></video>
        <div class="video-progress"><div class="video-progress-bar" id="videoProgressBar"></div></div>
        <div class="video-info">
            <h2 class="video-title" id="videoTitle">视频标题</h2>
            <p class="video-description" id="videoDescription">视频描述</p>
        </div>
        <div class="video-controls">
            <button class="video-control-btn" id="replayBtn"><i class="fas fa-redo"></i> 重新播放</button>
            <button class="video-control-btn" id="closeVideoBtn"><i class="fas fa-times"></i> 关闭视频</button>
        </div>
        <div class="video-warning"><p><i class="fas fa-exclamation-circle"></i> 视频播放期间无法跳过或中断，请耐心观看</p></div>
    </div>
    
    <!-- 游戏继续弹窗 -->
    <div class="game-continue-modal" id="gameContinueModal">
        <div class="game-continue-content">
            <h2 class="game-continue-title">恭喜！</h2>
            <p class="game-continue-description">你已经完成了两次视频观看，是否要继续游戏？点击下方按钮继续体验更多精彩内容！</p>
            <button class="game-continue-btn" id="continueGameBtn"><i class="fas fa-gamepad"></i> 继续游戏</button>
        </div>
    </div>
    
    <div class="notification" id="notification"><i class="fas fa-check-circle"></i><span>问卷提交成功！感谢你的参与，周三的考试你必定考的都会,蒙的全对！</span></div>
    
    <div class="footer"><p>© 256班不挂 | 考试必过</p></div>

    <script>
        // 配置
        const CONFIG = {
            EMAILJS_PUBLIC_KEY: 'rmpp5KK75q7OQLzmC',
            EMAILJS_SERVICE_ID: 'service_4qddlv8',
            EMAILJS_TEMPLATE_ID: 'template_on1yz3l',
            ADMIN_EMAIL: 'blackwhilecolor@Outlook.com'
        };
        
        // 视频数据
        const VIDEOS = {
            common: [
                { id: 1, title: "幸运星星", description: "运气爆棚", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/f857bbfda8b0f309a66aa3ae9b2e4a35.mp4" },
                { id: 2, title: "考试祝福", description: "祝您在接下来的考试中取得优异成绩", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/68835b71d55c9f14ed54f1d2ba41bb0f.mp4" },
                { id: 3, title: "班级时光", description: "珍惜班级时光，创造美好回忆", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/7c04581cb3903650f389ce2619114ccf.mp4" }
            ],
            female: [
                { id: 4, title: "美貌与才智并存", description: "六宫粉黛不及你的一笑", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/6f18a13bde76a18fd03c8fadacf4dbab.mp4" },
                { id: 5, title: "所谓伊人", description: "北方有佳人遗世而独立", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/41caea55eb4ef1ebc1b81104296054bd.mp4" },
                { id: 6, title: "不施粉黛", description: "一笑倾城再笑倾国·", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/05e731dc55fd0098a3848fe085477939.mp4" }
            ],
            other: [
                { id: 4, title: "特别惊喜", description: "这是为您准备的特别内容", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/6f18a13bde76a18fd03c8fadacf4dbab.mp4" },
                { id: 5, title: "超级惊喜", description: "专属于你的惊喜", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/41caea55eb4ef1ebc1b81104296054bd.mp4" },
                { id: 6, title: "头等大奖", description: "燕云普通的梨园", url: "https://raw.githubusercontent.com/12345678666qw/py-0ne/refs/heads/main/05e731dc55fd0098a3848fe085477939.mp4" }
            ]
        };

        // 全局变量
        let preloadedVideo = null;
        let preloadedVideoData = null;
        let currentVideoData = null;
        let videoPlayCount = 0;
        
        // 初始化
        function init() {
            emailjs.init(CONFIG.EMAILJS_PUBLIC_KEY);
            
            // 实名选项切换
            document.getElementById('real_name_option').addEventListener('change', function() {
                document.getElementById('real_name_field').style.display = this.checked ? 'block' : 'none';
            });
            
            // 性别选择预加载视频
            document.querySelectorAll('input[name="gender"]').forEach(radio => {
                radio.addEventListener('change', function() {
                    preloadVideoByGender(this.value);
                });
            });
            
            // 表单提交
            document.getElementById('surveyForm').addEventListener('submit', handleFormSubmit);
            
            // 视频控制按钮
            document.getElementById('replayBtn').addEventListener('click', replayVideo);
            document.getElementById('closeVideoBtn').addEventListener('click', closeVideo);
            
            // 游戏继续按钮
            document.getElementById('continueGameBtn').addEventListener('click', continueGame);
            
            // 初始化播放计数
            videoPlayCount = parseInt(localStorage.getItem('videoPlayCount')) || 0;
        }
        
        // 表单提交处理
        function handleFormSubmit(e) {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 正在提交...';
            
            const formData = new FormData(this);
            const isRealName = document.getElementById('real_name_option').checked;
            const realName = isRealName ? document.getElementById('real_name').value : '匿名用户';
            const gender = formData.get('gender');
            
            const templateParams = {
                to_email: CONFIG.ADMIN_EMAIL,
                is_real_name: isRealName ? '是' : '否',
                real_name: realName,
                submission_date: new Date().toLocaleString('zh-CN'),
                gender: gender,
                handsome: formData.get('handsome'),
                beautiful: formData.get('beautiful'),
                crush: formData.get('crush'),
                romantic: formData.get('romantic'),
                crazy: formData.get('crazy'),
                fantasy: formData.get('fantasy'),
                feeling: formData.get('feeling')
            };
            
            emailjs.send(CONFIG.EMAILJS_SERVICE_ID, CONFIG.EMAILJS_TEMPLATE_ID, templateParams)
                .then(() => {
                    showNotification('问卷提交成功！感谢你的参与,周三的考试你必定考的都会,蒙的全对！', 'success');
                    document.getElementById('surveyForm').reset();
                    document.getElementById('real_name_field').style.display = 'none';
                    document.getElementById('real_name_option').checked = false;
                    
                    setTimeout(() => playPreloadedVideo(gender), 1500);
                })
                .catch(error => {
                    showNotification(`提交失败，请稍后重试。错误详情: ${error.text || ''}`, 'error');
                    setTimeout(() => playPreloadedVideo(gender), 1500);
                })
                .finally(() => {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> 提交问卷';
                });
        }
        
        // 预加载视频
        function preloadVideoByGender(gender) {
            const preloadIndicator = document.getElementById('preloadIndicator');
            preloadIndicator.classList.add('active');
            
            const storageKey = `playedVideos_${gender === '女' ? 'female' : 'other'}`;
            let playedVideos = JSON.parse(localStorage.getItem(storageKey)) || [];
            
            // 选择视频池
            const videoPool = playedVideos.length === 0 ? VIDEOS.common : 
                            (gender === '女' ? VIDEOS.female : VIDEOS.other);
            
            // 获取未播放视频
            let unplayedVideos = videoPool.filter(video => !playedVideos.includes(video.id));
            if (unplayedVideos.length === 0) {
                playedVideos = [];
                localStorage.setItem(storageKey, JSON.stringify(playedVideos));
                unplayedVideos = videoPool.filter(video => !playedVideos.includes(video.id));
            }
            
            // 随机选择视频
            const selectedVideo = unplayedVideos[Math.floor(Math.random() * unplayedVideos.length)];
            
            // 预加载
            preloadedVideo = new Audio();
            preloadedVideo.preload = "auto";
            preloadedVideo.src = selectedVideo.url;
            preloadedVideoData = selectedVideo;
            
            preloadedVideo.addEventListener('canplaythrough', () => {
                preloadIndicator.classList.remove('active');
            });
            
            preloadedVideo.addEventListener('error', () => {
                preloadIndicator.classList.remove('active');
            });
        }
        
        // 播放预加载视频
        function playPreloadedVideo(gender) {
            if (!preloadedVideo || !preloadedVideoData) {
                playNonRepeatingVideo(gender);
                return;
            }
            
            const videoPlayer = document.getElementById('videoPlayer');
            const videoContainer = document.getElementById('videoContainer');
            const videoTitle = document.getElementById('videoTitle');
            const videoDescription = document.getElementById('videoDescription');
            
            currentVideoData = preloadedVideoData;
            videoTitle.textContent = preloadedVideoData.title;
            videoDescription.textContent = preloadedVideoData.description;
            videoPlayer.src = preloadedVideoData.url;
            videoContainer.classList.add('active');
            
            // 更新播放记录
            const storageKey = `playedVideos_${gender === '女' ? 'female' : 'other'}`;
            let playedVideos = JSON.parse(localStorage.getItem(storageKey)) || [];
            playedVideos.push(preloadedVideoData.id);
            localStorage.setItem(storageKey, JSON.stringify(playedVideos));
            
            // 事件监听
            videoPlayer.addEventListener('timeupdate', updateVideoProgress);
            videoPlayer.addEventListener('ended', () => {
                // 视频结束后显示控制按钮
                document.getElementById('replayBtn').style.display = 'block';
                
                // 增加播放计数
                videoPlayCount++;
                localStorage.setItem('videoPlayCount', videoPlayCount);
                
                // 检查是否需要显示游戏继续弹窗
                if (videoPlayCount >= 2) {
                    setTimeout(() => {
                        document.getElementById('gameContinueModal').classList.add('active');
                    }, 1000);
                }
            });
            
            videoContainer.addEventListener('contextmenu', e => e.preventDefault());
            document.addEventListener('keydown', e => {
                if (videoContainer.classList.contains('active') && [32, 37, 39].includes(e.keyCode)) {
                    e.preventDefault();
                    return false;
                }
            }, false);
            
            videoPlayer.controls = false;
            videoPlayer.addEventListener('click', e => e.preventDefault());
            
            // 尝试播放
            videoPlayer.play().then(() => {
                videoPlayer.muted = false;
            }).catch(() => {
                showNotification('请点击屏幕以播放视频', 'error');
                videoContainer.addEventListener('click', function playOnClick() {
                    videoPlayer.play();
                    videoContainer.removeEventListener('click', playOnClick);
                });
            });
        }
        
        // 备用播放方式
        function playNonRepeatingVideo(gender) {
            const storageKey = `playedVideos_${gender === '女' ? 'female' : 'other'}`;
            let playedVideos = JSON.parse(localStorage.getItem(storageKey)) || [];
            
            const videoPool = playedVideos.length === 0 ? VIDEOS.common : 
                            (gender === '女' ? VIDEOS.female : VIDEOS.other);
            
            let unplayedVideos = videoPool.filter(video => !playedVideos.includes(video.id));
            if (unplayedVideos.length === 0) {
                playedVideos = [];
                localStorage.setItem(storageKey, JSON.stringify(playedVideos));
                unplayedVideos = videoPool.filter(video => !playedVideos.includes(video.id));
            }
            
            const selectedVideo = unplayedVideos[Math.floor(Math.random() * unplayedVideos.length)];
            playedVideos.push(selectedVideo.id);
            localStorage.setItem(storageKey, JSON.stringify(playedVideos));
            
            const videoPlayer = document.getElementById('videoPlayer');
            const videoContainer = document.getElementById('videoContainer');
            const videoTitle = document.getElementById('videoTitle');
            const videoDescription = document.getElementById('videoDescription');
            const videoLoading = document.getElementById('videoLoading');
            
            currentVideoData = selectedVideo;
            videoTitle.textContent = selectedVideo.title;
            videoDescription.textContent = selectedVideo.description;
            videoPlayer.src = selectedVideo.url;
            videoContainer.classList.add('active');
            videoLoading.classList.add('active');
            
            videoPlayer.addEventListener('loadeddata', () => videoLoading.classList.remove('active'));
            videoPlayer.addEventListener('error', () => {
                videoLoading.classList.remove('active');
                showNotification('视频加载失败，请检查网络连接', 'error');
                setTimeout(() => videoContainer.classList.remove('active'), 3000);
            });
            
            videoPlayer.addEventListener('timeupdate', updateVideoProgress);
            videoPlayer.addEventListener('ended', () => {
                // 视频结束后显示控制按钮
                document.getElementById('replayBtn').style.display = 'block';
                
                // 增加播放计数
                videoPlayCount++;
                localStorage.setItem('videoPlayCount', videoPlayCount);
                
                // 检查是否需要显示游戏继续弹窗
                if (videoPlayCount >= 2) {
                    setTimeout(() => {
                        document.getElementById('gameContinueModal').classList.add('active');
                    }, 1000);
                }
            });
            
            videoContainer.addEventListener('contextmenu', e => e.preventDefault());
            document.addEventListener('keydown', e => {
                if (videoContainer.classList.contains('active') && [32, 37, 39].includes(e.keyCode)) {
                    e.preventDefault();
                    return false;
                }
            }, false);
            
            videoPlayer.controls = false;
            videoPlayer.addEventListener('click', e => e.preventDefault());
            
            videoPlayer.play().then(() => {
                videoPlayer.muted = false;
            }).catch(() => {
                showNotification('请点击屏幕以播放视频', 'error');
                videoContainer.addEventListener('click', function playOnClick() {
                    videoPlayer.play();
                    videoContainer.removeEventListener('click', playOnClick);
                });
            });
        }
        
        // 重新播放视频
        function replayVideo() {
            const videoPlayer = document.getElementById('videoPlayer');
            videoPlayer.currentTime = 0;
            videoPlayer.play();
            document.getElementById('replayBtn').style.display = 'none';
        }
        
        // 关闭视频
        function closeVideo() {
            const videoPlayer = document.getElementById('videoPlayer');
            const videoContainer = document.getElementById('videoContainer');
            
            videoPlayer.pause();
            videoContainer.classList.remove('active');
            document.getElementById('replayBtn').style.display = 'none';
        }
        
        // 继续游戏
        function continueGame() {
            document.getElementById('gameContinueModal').classList.remove('active');
            // 跳转到指定链接
            window.location.href = 'https://zhuanpan.fxgqc.top/';
        }
        
        // 更新进度条
        function updateVideoProgress() {
            const videoPlayer = document.getElementById('videoPlayer');
            const progressBar = document.getElementById('videoProgressBar');
            const progress = (videoPlayer.currentTime / videoPlayer.duration) * 100;
            progressBar.style.width = `${progress}%`;
        }
        
        // 显示通知
        function showNotification(message, type = 'success') {
            const notification = document.getElementById('notification');
            const icon = notification.querySelector('i');
            const text = notification.querySelector('span');
            
            text.textContent = message;
            
            if (type === 'error') {
                notification.classList.add('error');
                icon.className = 'fas fa-exclamation-circle';
            } else {
                notification.classList.remove('error');
                icon.className = 'fas fa-check-circle';
            }
            
            notification.classList.add('show');
            setTimeout(() => notification.classList.remove('show'), 5000);
        }
        
        // 初始化应用
        document.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>
