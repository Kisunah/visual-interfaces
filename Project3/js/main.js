d3.csv('data/showData.csv')
    .then(_data => {
        console.log('Data loading complete');

        let data = _data;

        let mainCharacterList = ['HOUSE', 'WILSON', 'CAMERON', 'CHASE', 'FOREMAN', 'CUDDY', 'KUTNER', 'TAUB', 'THIRTEEN', 'MASTERS', 'ADAMS', 'PARK', 'STACY', 'AMBER']; // Characters with > 250 lines of dialogue

        

        let characterLineData = {};
        // seasonLineCount = {};

        data.forEach((item) => {
            if (characterLineData[item.Character] == undefined) characterLineData[item.Character] = 1;
            else characterLineData[item.Character] += 1;
        });

        let temp = [];
        mainCharacterList.forEach((character) => {
            let obj = {
                character: character,
                count: characterLineData[character]
            };
            temp.push(obj);
        });
        characterLineData = temp;
        
        console.log(characterLineData);

        let characterLineCountChart = new CharacterLineCountChart({ parentElement: '#characterLineCountChart' }, characterLineData);
    });